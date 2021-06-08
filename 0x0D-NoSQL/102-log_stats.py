#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    c = list(nginx_collection.find())
    i = {}
    z = len(c)
    print(z, "logs\nMethods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        print(
            "\tmethod {}: {}".format(
                m, len(list(nginx_collection.find({"method": m})))
                )
            )
    print(
        "{} status check".format(
            len(list(
                nginx_collection.find({"method": "GET", "path": "/status"})
                ))
            )
        )
    for log in c:
        if log.get('ip') and log.get('ip') in i:
            i[log.get('ip')] += 1
        elif log.get('ip'):
            i[log.get('ip')] = 1
    print("i:")
    for ip in sorted(i, key=i.get, reverse=True)[:10]:
        print("\t{}: {}".format(ip, i[ip]))