from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import login


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
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'handle')
        
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log them in immediately after signup
            return redirect('account')
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/signup.html', {'form': form})

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