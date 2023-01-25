#!/usr/bin/env python3
"""
class LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache"""
    def __init__(self):
        """Initializing class LIFOCaching"""
        super().__init__()
        self.lastKey = ""

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value
        for the key key"""
        if (key and item):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                print(f"DISCARD: {self.lastKey}")
                self.cache_data.pop(self.lastKey)
            self.lastKey = key

    def get(self, key):
        """return the value in
        self.cache_data linked to key"""
        if (key is None or key not in self.cache_data):
            return None
        else:
            return self.cache_data[key]
