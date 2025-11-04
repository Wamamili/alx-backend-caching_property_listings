from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from django.core.cache import cache

@cache_page(60 * 15)  # Cache response for 15 minutes
def property_list(request):
    cache_key = "all_properties"
    properties = cache.get(cache_key)
    
    if not properties:
        properties = list(Property.objects.all().values("id", "title", "description", "price", "location", "created_at"))
        cache.set(cache_key, properties, timeout=60 * 15)  # Cache for 15 minutes
    
    return JsonResponse(properties, safe=False)
