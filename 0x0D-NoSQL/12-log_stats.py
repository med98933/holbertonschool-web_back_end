#!/usr/bin/env python3
"""Print info f nginx logs """
from pymongo import MongoClient

if __name__ == "__main__":
    """ a Python script that provides some stats about
    Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    n_collection = client.logs.nginx

    print(f"{n_collection.estimated_document_count()} logs")

    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = n_collection.count_documents({'method': m})
        print(f"\tmethod {m}: {method_count}")

    check_get = n_collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print(f"{check_get} status check")
