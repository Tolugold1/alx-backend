#!/usr/bin/env python3
"""function named index_range that
takes two integer arguments page and
page_size"""


def index_range(page: int, page_size: int) -> tuple:
    """indexing function"""
    stp = (page - 1) * page_size #stp - start page
    edp = (stp + page_size) #edp - end page
    t = (stp, edp)
    return t
