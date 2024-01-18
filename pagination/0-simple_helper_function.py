#!/usr/bin/env python3
"""task 0 """

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns the corresponding index"""
    start_page = (page - 1) * page_size
    return (start_page, start_page + page_size)