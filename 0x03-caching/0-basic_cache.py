#!/usr/bin/python3
"""
Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
           return the value
        """
        return self.cache_data.get(key)
