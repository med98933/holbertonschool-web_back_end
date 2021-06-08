#!/usr/bin/env python3
"""  MongoDB insert """


def insert_school(mongo_collection, **kwargs):
    """ function that inserts in school collection a document"""
    m = mongo_collection.insert_one(kwargs)
    return m.inserted_id
