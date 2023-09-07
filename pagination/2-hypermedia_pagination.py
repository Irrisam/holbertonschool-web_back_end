#!/usr/bin/env python3
"""file for retrieving data from a database of popular baby names."""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """function that returns starting values and ending pagination indexes"""
    end_index = (page * page_size)
    start_index = end_index - page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function that returns"""
        assert isinstance(page, int) and page >= 0
        assert isinstance(page_size, int) and page_size >= 0
        data = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(data):
            return []

        result = data[start_index:end_index]

        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets key values dict of values"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.get_page(page, page_size)
        next_page = self.get_page(page + 1, page_size)
        prev_page = self.get_page(page - 1, page_size)

        try:
            total_pages = math.ceil(len(self.dataset()) / page_size)
        except ZeroDivisionError:
            total_pages = 0

        result_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if next_page else None,
            'prev_page': page - 1 if prev_page else None,
            'total_pages': total_pages
        }

        return result_dict
