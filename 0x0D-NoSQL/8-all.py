#!/usr/bin/env python3
"""  pymongo list  """


def list_all(mongo_collection):
    """ List all elements in a collection """
    m = mongo_collection.find()
    return m if m else []