#!/usr/bin/python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Class that inherits from
    BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value
        for the key key"""
        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
        else:
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            self.cache_data[key] = item
            print(f"DISCARD: {first_key}")

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
