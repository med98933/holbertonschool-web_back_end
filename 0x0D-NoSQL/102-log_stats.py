#!/usr/bin/env python3
"""
 Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db_nginx = client.logs.nginx
    all = list(db_nginx.find())
    ips = {}
    x = len(all)
    print(x, "logs\nMethods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        print(
            "\tmethod {}: {}".format(
                m, len(list(db_nginx.find({"method": m})))
                )
            )
    print(
        "{} status check".format(
            len(list(
                db_nginx.find({"method": "GET", "path": "/status"})
                ))
            )
        )
    for count in all:
        if count.get('ip') and count.get('ip') in ips:
            ips[count.get('ip')] += 1
        elif count.get('ip'):
            ips[count.get('ip')] = 1
    print("IPs:")
    for ip in sorted(ips, key=ips.get, reverse=True)[:10]:
        print("\t{}: {}".format(ip, ips[ip]))