#!/usr/bin/env python3
"""
Implement a method named get_page
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """indexing function"""
    stp = (page - 1) * page_size  # stp - start page
    edp = (stp + page_size)  # edp - end page
    t = (stp, edp)
    return t


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
        """implement get_page"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        stf, edf = index_range(page, page_size)
        page_of_dataset = []
        if (stf >= len(self.dataset())):
            return page_of_dataset
        page_of_dataset = self.dataset()
        return page_of_dataset[stf:edf]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function returns a dictionary
        containing the following key-value
        pairs"""
        p_data = self.get_page(self, page, page_size)
        if (len(p_data) > 1):
            next_page = page + 1
        else:
            next_page = None
        if (page != 0):
            prev_page = page - 1
        else:
            prev_page = None
        total_pages = math.floor(len(self.dataset()) / page_size)
        return {"page_size": page_size, "page": page,
                "data": p_data, "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages}
