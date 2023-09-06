#!/usr/bin/env python3
"""function updating topics dependind on name"""


def update_topics(mongo_collection, name, topics):
    """function updating topics dependind on name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
