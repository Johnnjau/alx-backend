#!/usr/bin/env python3
"""the Basic cache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def __init__(self):
        """class constructor method"""
        super().__init__()

    def put(self, key, item):
        """add Item intto the cache dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data or None"""
        return self.cache_data.get(key, None)
