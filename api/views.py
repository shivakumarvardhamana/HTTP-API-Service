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
