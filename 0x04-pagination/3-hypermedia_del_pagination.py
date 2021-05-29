#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [r for r in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The method should return a dictionary
        """
        assert (isinstance(index, int)
                and index in range(len(self.__indexed_dataset)))
        data = []
        dif = 0
        r = index
        while dif < page_size and r < len(self.__indexed_dataset):
            if r in self.__indexed_dataset:
                data.append(self.__indexed_dataset[r])
                r += 1
                dif += 1
            else:
                r += 1
        if r < len(self.__indexed_dataset):
            next = r
        else:
            next = None
        return {'index': index, 'next_index': next,
                'page_size': len(data), 'data': data}