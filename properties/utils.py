from django.core.cache import cache
from .models import Property

def get_all_properties():
    cached_properties = cache.get('all_properties')
    if cached_properties is not None:
        return cached_properties

    queryset = Property.objects.all()
    cache.set('all_properties', queryset, 3600)
    return queryset
