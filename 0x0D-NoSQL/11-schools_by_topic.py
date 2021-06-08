#!/usr/bin/env python3
""" MongoDB Find"""


def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list of school having a specific topic
    """
    return [x for x in mongo_collection.find({"topics": topic})]
