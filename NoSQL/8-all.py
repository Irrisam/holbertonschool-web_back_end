def list_all(mongo_collection):
    cursor = mongo_collection.find({})
    docs = []

    for doc in cursor:
        docs.append(doc)

    return docs
