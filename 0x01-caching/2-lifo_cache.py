#!/usr/bin/python3
"""LIFO Caching class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Class"""
    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """Add items to cache"""
        if not (key and item):
            return None
        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f'DISCARD: {list(self.cache_data.keys())[-2]}')
            del self.cache_data[list(self.cache_data.keys())[-2]]

    def get(self, key):
        """ find item using key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
