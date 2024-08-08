# # from django.urls import path,include
# # from .views import blog_api,likes_api,user_api,user_owner

# # from rest_framework.routers import DefaultRouter
# # router=DefaultRouter()
# # import rest_framework
# # # router.register('api',blog_api,basename="api")
# # # router.register('api1',likes_api,basename="api1")
# # # router.register('api2',user_api,basename="api2")
# # router.register('api4',user_owner,basename="api4")
# # urlpatterns=[
# #     path('',include(router.urls)),
# #     path('api',include('rest_framework.urls')),

# # ]

# # urls.py
# from django.urls import path
# # from . import views
# from .views import KeyValueStoreView, SearchView

# urlpatterns = [
#     # path('get/', views.EmployeeList.as_view(), name='employee-list'),
#     # path('create/', views.EmployeeCreate.as_view(), name='employee-create'),
#     path("get/<str:key>", KeyValueStoreView.as_view()),
#     path("set", KeyValueStoreView.as_view()),
#     path("search", SearchView.as_view()),
# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('set', set_key_value, name='set_key_value'),
        path('get/<str:key>', get_value, name='get_value'),  # Handles GET requests to fetch a value by key
    path('search', search_keys, name='search_keys'), 
]