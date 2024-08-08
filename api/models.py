
   # models.py
from django.db import models

# class Employee1(models.Model):
#     username = models.CharField(max_length=100)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username
# class KeyValueStore(models.Model):
#     key = models.CharField(max_length=255, primary_key=True)
#     value = models.CharField(max_length=255)
from django.db import models

class KeyValue(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}: {self.value}"
