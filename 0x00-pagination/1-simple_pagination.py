#!/usr/bin/env python3
"""
Implement a method named get_page
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """indexing function"""
    stp = (page - 1) * page_size #stp - start page
    edp = (stp + page_size) #edp - end page
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
            stp = page
            edf = page_size
            t = index_range(stp, edf)
            if (stp >= len(self.dataset())):
                return []
            page_of_dataset = self.dataset()
            return page_of_dataset[stp:edf]
