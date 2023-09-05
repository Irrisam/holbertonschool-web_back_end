#!/usr/bin/env python3
"""adds multiple docs a collection inputed"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """adds multiple docs a collection inputed"""
    client = MongoClient()
    db = client("school")
    collection = db[mongo_collection]

    collection.insert(kwargs)

    client.close
