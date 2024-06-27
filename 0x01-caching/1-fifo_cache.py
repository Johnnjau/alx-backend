#!/usr/bin/python3
""" FIFO Class"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Class"""
    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """If key or item is None
        method should not do anything"""
        if not (key and item):
            return None
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f'DISCARD: {list(self.cache_data.keys())[0]}')
            del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """ Find items using key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
