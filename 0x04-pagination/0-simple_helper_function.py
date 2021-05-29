#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
  Return:
            tuple with the range start and end size page
    """
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
