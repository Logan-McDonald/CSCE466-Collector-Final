from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q, Max
from django.db.models.functions import Greatest
from .models import Message

User = get_user_model()

@login_required
def index(request):
    handle = request.GET.get('handle')
    first_message = request.GET.get('first_message')
    if handle:
        other = get_object_or_404(User, handle=handle)
        if first_message:
            Message.objects.create(
                sender=request.user,
                receiver=other,
                content=first_message
            )
        return redirect('chat', handle=handle)

    contacts = User.objects.filter(
        Q(sent_messages__receiver=request.user) |
        Q(received_messages__sender=request.user)
    ).distinct().annotate(
        last_sent=Max('sent_messages__timestamp'),
        last_received=Max('received_messages__timestamp'),
    ).annotate(
        last_msg=Greatest('last_sent', 'last_received')
    ).order_by('-last_msg')

    return render(request, 'messaging/index.html', {
        'contacts': contacts,
    })

@login_required
def chat_room(request, handle):
    other = get_object_or_404(User, handle=handle)

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            Message.objects.create(
                sender=request.user,
                receiver=other,
                content=content
            )
        return redirect('chat', handle=handle)

    contacts = User.objects.filter(
        Q(sent_messages__receiver=request.user) |
        Q(received_messages__sender=request.user)
    ).distinct().annotate(
        last_sent=Max('sent_messages__timestamp'),
        last_received=Max('received_messages__timestamp'),
    ).annotate(
        last_msg=Greatest('last_sent', 'last_received')
    ).order_by('-last_msg')

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other) |
        Q(sender=other, receiver=request.user)
    ).order_by('timestamp')

    users = sorted([request.user.handle, other.handle])
    room_key = '_'.join(users)

    return render(request, 'messaging/chat_room.html', {
        'room_handle': handle,
        'contacts': contacts,
        'messages': messages,
        'my_handle': request.user.handle,
        'room_key': room_key,
    })
