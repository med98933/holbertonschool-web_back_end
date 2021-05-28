#!/usr/bin/python3
"""MRU Caching
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ BaseCache
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
                most_recently_used_item_key = sorted_dict_keys[-2]
                del self.cache_by_time[most_recently_used_item_key]
                del self.cache_data[most_recently_used_item_key]
                print('DISCARD: {}'.format(most_recently_used_item_key))

    def get(self, key):
        """
            Return linked to key
        """
        value = self.cache_data.get(key)
        if value:
            self.cache_by_time[key] = datetime.now()
        return value
