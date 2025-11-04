from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property

CACHE_KEY = "all_properties"

@receiver(post_save, sender=Property)
def clear_cache_on_save(sender, instance, **kwargs):
    cache.delete(CACHE_KEY)
    print("Cache invalidated after Property save.")

@receiver(post_delete, sender=Property)
def clear_cache_on_delete(sender, instance, **kwargs):
    cache.delete(CACHE_KEY)
    print("Cache invalidated after Property delete.")
