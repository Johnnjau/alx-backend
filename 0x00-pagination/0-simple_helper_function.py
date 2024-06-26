#!/usr/bin/env python3
"""return (start index, end)"""


def index_range(page: int, page_size: int) -> tuple:
    """ retrn start, end indeces"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
