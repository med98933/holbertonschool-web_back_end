#!/usr/bin/python3
""" LFUCache
"""
from datetime import datetime
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache Class """
    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_by_time = {}
        self.cache_by_frequency_use = defaultdict(int)

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_by_time[key] = datetime.now()
            self.cache_data[key] = item
            self.cache_by_frequency_use[key] += 1

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                frequency_use_filtered = {}
                for k, v in self.cache_by_frequency_use.items():
                    if k != key:
                        frequency_use_filtered[k] = v
                keys_by_frequency_used = sorted(frequency_use_filtered,
                                                key=frequency_use_filtered.get)
                key_to_delete = keys_by_frequency_used[0]

                count = frequency_use_filtered[key_to_delete]
                posibles_es_to_discard_dict = {}
                for k, v in frequency_use_filtered.items():
                    if v == count:
                        posibles_es_to_discard_dict[k] = v
                if len(posibles_es_to_discard_dict) > 1:
                    es_to_discard_by_time = {}
                    for k, v in self.cache_by_time.items():
                        if k in posibles_es_to_discard_dict.keys():
                            es_to_discard_by_time[k] = v

                    es_by_time = sorted(
                                          es_to_discard_by_time,
                                          key=es_to_discard_by_time.get)
                    key_to_delete = es_by_time[0]

                del self.cache_by_time[key_to_delete]
                del self.cache_data[key_to_delete]
                del self.cache_by_frequency_use[key_to_delete]
                print('DISCARD: {}'.format(key_to_delete))

    def get(self, key):
        """return the value of key in self.cache_data"""
        e = self.cache_data.get(key)
        if e:
            self.cache_by_time[key] = datetime.now()
            self.cache_by_frequency_use[key] += 1
        return e
