# # from rest_framework import serializers

# # from django.contrib.auth.models import User
# # from . models import blog,likes
# # class blogser(serializers.ModelSerializer):
# #     # user=serializers.CharField(read_only=True)
# #     class Meta:
# #         model=blog
# #         fields='__all__'

# # class likeser(serializers.ModelSerializer):
# #     # user=serializers.CharField(read_only=True)
# #     class Meta:
# #         model=likes
# #         # fields=['likes_total_count']
# #         fields='__all__'
# # class userser(serializers.ModelSerializer):
# #     class Meta:
# #         model=User
# #         fields='__all__'

# # serializers.py
# from rest_framework import serializers
# from .models import Employee1

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee1
#         fields = ['id', 'username', 'salary', 'location']

# # serializers.py
# from rest_framework import serializers
# from .models import Employee1

# class EmployeeCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee1
#         fields = ['username', 'salary', 'location']

from rest_framework import serializers
from .models import KeyValue

class KeyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyValue
        fields = ['key', 'value']
