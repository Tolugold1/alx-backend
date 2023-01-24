#!/usr/bin/env python3
"""
class FIFOCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__("BaseCaching").BaseCaching


class FIFOCache(BaseCaching):
    """class fifo caching"""
    def __init__(self):
        """Initializing class FIFOCaching"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value
        for the key key"""
        if (key is not None and item is not None):
            self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            lst = []
            for x in self.cache_data.keys():
                lst.append(x)
            del self.cache_data[lst[0]]
            print(f"DISCARD: {lst[0]}")

    def get(self, key):
        """return the value in
        self.cache_data linked to key"""
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
