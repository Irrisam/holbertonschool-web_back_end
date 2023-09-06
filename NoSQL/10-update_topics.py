#!/usr/bin/env python3
"""function updating topics dependind on name"""


def update_topics(mongo_collection, name, topics):
    """function updating topics dependind on name"""
    result = mongo_collection.updateMany({"name": name},
                                         {"$set": {"topics": topics}})
    return result
