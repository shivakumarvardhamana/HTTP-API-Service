# # from django.shortcuts import render,HttpResponse
# # from .serializers import blogser,likeser,userser
# # from . models import blog,likes
# # from rest_framework import viewsets
# # from django.contrib.auth.models import User
# # from rest_framework.authentication import SessionAuthentication
# # from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
# # # from rest_framework.generics import ListAPIView
# # # Create your views here.



# # # the owner of his blog only acces the data and do CRUD operations for him self with this API

# # # Thank you!..


# # class blog_api(viewsets.ModelViewSet):
# #     queryset=blog.objects.all()
# #     serializer_class=blogser
# #     authentication_classes=[SessionAuthentication]
# #     permission_classes=[IsAuthenticated]
# #     def get_queryset(self):
# #         user1=self.request.user
        
# #         print(user1)
# #         return blog.objects.filter(user=user1)

# # #The owner of his likes he can only acces and do CRUD operation for him self with this API

# # # Thank you!..


# # class likes_api(viewsets.ModelViewSet):
# #     queryset=likes.objects.all()
# #     serializer_class=likeser
# #     authentication_classes=[SessionAuthentication]
# #     permission_classes=[IsAuthenticated]
# #     def get_queryset(self):
# #         user1=self.request.user
        
# #         print(user1)
# #         return likes.objects.filter(user=user1)

# # #owner of the account can only access this api data and can do CRUD operation for him self with this API

# # # Thank you!..


# # class user_owner(viewsets.ModelViewSet):
# #     queryset=User.objects.all()
# #     serializer_class=userser
# #     authentication_classes=[SessionAuthentication]
# #     permission_classes=[IsAuthenticated]
# #     def get_queryset(self):
# #         pk=self.request.user

# #         return (User.objects.filter(username=pk))


# # #this is superuser alias ADMIN He have all accounts acces hhe can do anu CRUD operations with this API

# # # Thank you!..

# # class user_api(viewsets.ModelViewSet):
# #     queryset=User.objects.all()
# #     serializer_class=userser
# #     authentication_classes=[SessionAuthentication]
# #     permission_classes=[IsAdminUser]
# #     # def get_queryset(self):
# #     #     user1=self.request.user
        
# #     #     print(user1)
# #     #     return User.objects.filter(user=user1)
        


# # views.py
# from rest_framework import generics
# #from .models import Employee1

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import KeyValueStore

# class KeyValueStoreView(APIView):
#     def get(self, request, key):
#         try:
#             value = KeyValueStore.objects.get(key=key).value
#             return Response({"value": value})
#         except KeyValueStore.DoesNotExist:
#             return Response({"error": "Key not found"}, status=404)

#     def post(self, request):
#         key = request.data.get("key")
#         value = request.data.get("value")
#         if key and value:
#             KeyValueStore.objects.update_or_create(key=key, defaults={"value": value})
#             return Response({"message": "Key-value pair set successfully"})
#         return Response({"error": "Key and value are required"}, status=400)

# class SearchView(APIView):
#     def get(self, request):
#         prefix = request.GET.get("prefix")
#         suffix = request.GET.get("suffix")
#         keys = KeyValueStore.objects.all()
#         if prefix:
#             keys = keys.filter(key__startswith=prefix)
#         if suffix:
#             keys = keys.filter(key__endswith=suffix)
#         return Response({"keys": [key.key for key in keys]})


# # from .serializers import EmployeeSerializer

# # class EmployeeList(generics.ListCreateAPIView):
# #     queryset = Employee1.objects.all()
# #     serializer_class = EmployeeSerializer

# # views.py
# # from rest_framework import generics
# # from .models import Employee
# # from .serializers import EmployeeCreateSerializer

# # class EmployeeCreate(generics.CreateAPIView):
# #     queryset = Employee1.objects.all()
# #     serializer_class = EmployeeCreateSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import KeyValue


@csrf_exempt  # Exempt this view from CSRF verification (for simplicity)
def set_key_value(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            key = data.get('key')
            value = data.get('value')
            
            if not key or not value:
                return JsonResponse({"error": "Key and value are required"}, status=400)

            # If using the database model
            # key_value, created = KeyValue.objects.update_or_create(key=key, defaults={'value': value})

            # If not using a database, store in memory (e.g., a global dictionary)
            # In-memory dictionary (not persistent)
            global key_value_store
            if not 'key_value_store' in globals():
                key_value_store = {}
            key_value_store[key] = value

            return JsonResponse({"success": True, "key": key, "value": value})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
@csrf_exempt
def get_value(request, key):
    try:
        key_value = KeyValue.objects.get(key=key)
        return JsonResponse({"key": key_value.key, "value": key_value.value})
    except KeyValue.DoesNotExist:
        return JsonResponse({"error": "Key not found"}, status=404)

@csrf_exempt
def search_keys(request):
    prefix = request.GET.get('prefix')
    suffix = request.GET.get('suffix')

    if not prefix and not suffix:
        return JsonResponse({"error": "Prefix or suffix query parameter is required"}, status=400)

    if prefix:
        matching_keys = KeyValue.objects.filter(key__startswith=prefix)
    elif suffix:
        matching_keys = KeyValue.objects.filter(key__endswith=suffix)

    keys = [kv.key for kv in matching_keys]

    return JsonResponse({"keys": keys})
