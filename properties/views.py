from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()

    data = [
        {
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": str(item.price),
            "location": item.location,
            "created_at": item.created_at.isoformat()
        }
        for item in properties
    ]

    return JsonResponse(data, safe=False)
