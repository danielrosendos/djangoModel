import jwt

from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_cache(name=None):
    if name in cache:
        return cache.get(name)

    return None


def set_cache(name=None, payload=None):
    cache.set(name, payload, timeout=CACHE_TTL)


def decode_token(token=None):
    return jwt.decode(
        token,
        getattr(settings, 'SIMPLE_JWT').get('SIGNING_KEY'),
        algorithms=[getattr(settings, 'SIMPLE_JWT').get('ALGORITHM')]
    )
