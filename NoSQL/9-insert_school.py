#!/usr/bin/env python3
"""adds multiple docs a collection inputed"""


def insert_school(mongo_collection, **kwargs):
    """adds multiple docs a collection inputed"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
