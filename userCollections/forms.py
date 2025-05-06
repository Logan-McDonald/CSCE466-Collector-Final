from django import forms
from .models import Collection, Item

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['title']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'image']
