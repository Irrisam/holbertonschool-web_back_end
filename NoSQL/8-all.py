#!/usr/bin/env python3
"""function that returns a list of all documents in a mongo collection"""


def list_all(mongo_collection):
    """function that returns a list of all documents in a mongo collection."""
    cursor = mongo_collection.find({})
    docs = []

    for doc in cursor:
        docs.append(doc)

    return docs
