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
        # Handle creating a new collection
        if 'create_collection' in request.POST:
            collection_form = CollectionForm(request.POST)
            if collection_form.is_valid():
                new_collection = collection_form.save(commit=False)
                new_collection.user = request.user
                new_collection.save()
                return redirect('profile')  # Make sure to return a response after creating

        # Handle adding an item to a collection
        elif 'add_item' in request.POST:
            item_form = ItemForm(request.POST, request.FILES)
            collection_id = request.POST.get('collection_id')
            if item_form.is_valid() and collection_id:
                item = item_form.save(commit=False)
                item.collection_id = collection_id
                item.save()
                return redirect('profile')  # Ensure a redirect after adding an item

        # Handle removing an item from a collection
        elif 'remove_item' in request.POST:
            item_id = request.POST.get('item_id')
            if item_id:
                item = Item.objects.get(id=item_id)
                item.delete()
                return redirect('profile')  # Redirect after removing an item

        # Handle removing a collection
        elif 'remove_collection' in request.POST:
            collection_id = request.POST.get('collection_id')
            if collection_id:
                collection = Collection.objects.get(id=collection_id, user=request.user)
                collection.delete()
                return redirect('profile')  # Redirect after removing a collection

    # If the request is GET, render the profile view
    return render(request, 'userCollections/profile.html', {
        'collections': collections,
        'collection_form': collection_form,
        'item_form': item_form,
    })

