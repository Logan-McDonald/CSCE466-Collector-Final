from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.models import CustomUser
from django import forms
from django.contrib.auth import logout


class HandleUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['handle']
        widgets = {
            'handle': forms.TextInput(attrs={
                'placeholder': 'Your unique handle',
                'class': 'form-control',
            })
        }

@login_required
def account(request):
    user = request.user
    if request.method == 'POST':
        form = HandleUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = HandleUpdateForm(instance=user)

    return render(request, 'account/account.html', {
        'form': form,
        'user': user,
    })

def login_redirect(request):
    logout(request)
    return redirect('login')