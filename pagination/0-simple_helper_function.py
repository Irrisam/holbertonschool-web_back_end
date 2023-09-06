#!/usr/bin/env python3
"""function that returns starting values and ending pagination indexes"""


def index_range(page: int, page_size: int):
    """function that returns starting values and ending pagination indexes"""
    end_index = (page * page_size)
    start_index = end_index - page_size

    return (start_index, end_index)
