#!/usr/bin/env python3
"""
caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRU caching"""
    def __init__(self):
        """Class that inherits from
        BaseCaching and is a caching system"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value
        for the key key"""
        if Key and item:
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS):
                if (key in self.cache_data):
                    del self.cache_data[key]
                self.cache_data[key] = item
            else:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.cache_data[key] = item
                else:
                    last_key = list(self.cache_data.keys())[-1]
                    del self.cache_data[last_key]
                    self.cache_data[key] = item
                    print(f"DISCARD: {last_key}")

    def get(self, key):
        """return the value in
        self.cache_data linked to key"""
        if key is None:
            return None
        if key in self.cache_data:
            temp = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = temp
            return temp
