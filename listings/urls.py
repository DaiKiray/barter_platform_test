from django.urls import path
from .views import create_listing, edit_listing, listing_detail  
urlpatterns = [
    path('create/', create_listing, name='create_listing'),
    path('edit/<int:listing_id>/', edit_listing, name='edit_listing'),
    path('detail/<int:listing_id>/', listing_detail, name='listing_detail'),
]
