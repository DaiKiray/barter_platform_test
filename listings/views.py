from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from .forms import ListingForm

def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('listing_detail', listing_id=listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/create_listing.html', {'form': form})

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def edit_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.user != listing.user:
        return redirect('listing_detail', listing_id=listing.id)  
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', listing_id=listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/edit_listing.html', {'form': form, 'listing': listing})
