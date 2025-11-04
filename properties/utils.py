import logging
from django_redis import get_redis_connection

# Configure logger
logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieves Redis cache hit/miss metrics and calculates the hit ratio.

    Returns:
        dict: A dictionary containing hits, misses, and hit ratio.
    """
    try:
        # Get default Redis connection
        redis_conn = get_redis_connection("default")

        # Fetch Redis INFO statistics
        info = redis_conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses
        hit_ratio = (hits / total_requests) if total_requests > 0 else 0.0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": round(hit_ratio, 2),
        }

        # Log metrics for monitoring
        logger.info(f"Redis Cache Metrics: {metrics}")

        return metrics

    except Exception as e:
        logger.error(f"Error fetching Redis metrics: {e}")
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0.0,
            "error": str(e),
        }
