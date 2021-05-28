#!/usr/bin/python3
"""
LIFO Caching
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
      LIFO caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_by_time = {}

    def put(self, key, item):
        """
        Assign to the dictionary
        """
        if key and item:
            self.cache_by_time[key] = datetime.now()
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                sorted_dict_keys = sorted(
                                          self.cache_by_time,
                                          key=self.cache_by_time.get)
                penultimate_in__key_element = sorted_dict_keys[-2]
                del self.cache_by_time[penultimate_in__key_element]
                del self.cache_data[penultimate_in__key_element]
                print('DISCARD: {}'.format(penultimate_in__key_element))

    def get(self, key):
        """
            Return the value linked
        """
        return self.cache_data.get(key)
