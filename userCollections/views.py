from django.shortcuts import render, redirect
from .models import Collection, Item
from .forms import CollectionForm, ItemForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import CollectionForm, ItemForm
from .models import Collection, Item
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    print("Profile view accessed")
    
    collections = Collection.objects.filter(user=request.user).prefetch_related('items')
    collection_form = CollectionForm()
    item_form = ItemForm()

    if request.method == 'POST':
        if 'create_collection' in request.POST:
            collection_form = CollectionForm(request.POST)
            if collection_form.is_valid():
                new_collection = collection_form.save(commit=False)
                new_collection.user = request.user
                new_collection.save()
                return redirect('profile')

        elif 'add_item' in request.POST:
            item_form = ItemForm(request.POST, request.FILES)
            collection_id = request.POST.get('collection_id')
            if item_form.is_valid() and collection_id:
                item = item_form.save(commit=False)
                item.collection_id = collection_id
                item.save()
                return redirect('profile')

        elif 'remove_item' in request.POST:
            item_id = request.POST.get('item_id')
            if item_id:
                item = Item.objects.get(id=item_id)
                item.delete()
                return redirect('profile')

        elif 'remove_collection' in request.POST:
            collection_id = request.POST.get('collection_id')
            if collection_id:
                collection = Collection.objects.get(id=collection_id, user=request.user)
                collection.delete()
                return redirect('profile')

    return render(request, 'userCollections/profile.html', {
        'collections': collections,
        'collection_form': collection_form,
        'item_form': item_form,
    })

