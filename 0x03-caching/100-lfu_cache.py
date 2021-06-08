#!/usr/bin/python3
""" 100-lfu_cache.py"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(s):
        """Initiliaze """
        super().__init__()
        s.lfu_order = []
        s.frequency = {}

    def put(s, k, c):
        """
Add an c in the cache
        """
        if k is not None and c is not None:
            if k in s.cache_data:
                s.cache_data[k] = c
                s.frequency[k] += 1
                s.lfu_order.remove(k)
            else:
                if len(s.cache_data) >= s.MAX_cS:
                    min_value = min(s.frequency.values())
                    min_ks = [k for k in s.frequency
                            if s.frequency[k] == min_value]
                    for x in range(len(s.lfu_order)):
                        if s.lfu_order[x] in min_ks:
                            break
                    del s.cache_data[s.lfu_order[x]]
                    del s.frequency[s.lfu_order[x]]
                    print("DISCARD:", s.lfu_order[x])
                    s.lfu_order.pop(x)
                s.cache_data[k] = c
                s.frequency[k] = 1
            s.lfu_order.append(k)

    def get(s, k):
        """
        Get an c by k
        """
        if k in s.cache_data:
            s.lfu_order.remove(k)
            s.lfu_order.append(k)
            s.frequency[k] += 1
            return s.cache_data[k]
        return None
