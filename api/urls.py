from django.urls import path
from .views import *

urlpatterns = [
    path('set', set_key_value, name='set_key_value'),
        path('get/<str:key>', get_value, name='get_value'),  # Handles GET requests to fetch a value by key
    path('search', search_keys, name='search_keys'), 
]
