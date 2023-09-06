#!/usr/bin/env python3
"""function that returbs all schools that have given topics."""


def schools_by_topic(mongo_collection, topic):
    """function that returbs all schools that have given topics."""
    school_names = []

    for school in mongo_collection.find({"topics": topic}):
        school_names.append(school)
    return school_names
