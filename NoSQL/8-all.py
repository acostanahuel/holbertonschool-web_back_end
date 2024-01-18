#!/usr/bin/env python3
"""task 8"""


def list_all(mongo_collection):
    """Function to list all documents"""
    docs = mongo_collection.find()
    if not docs:
        return []
    return docs