#!/usr/bin/env python3
""" """


def schools_by_topic(mongo_collection, topic):
    """ """
    school_names = []

    for school in mongo_collection.find({"topics": topic}):
        school_names.append(school)
    return school_names
