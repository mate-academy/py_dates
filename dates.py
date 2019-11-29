"""module for work with date and time"""
from datetime import datetime


def dates_between(first: str, second: str) -> int:
    """return difference between two dates in days"""
    return abs((datetime.strptime(first, '%d.%m.%Y') - datetime.strptime(second, '%d.%m.%Y')).days)
