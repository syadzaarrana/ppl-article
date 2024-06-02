from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_json

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('json/', show_wishlist_json, name='show_wishlist_json')
]