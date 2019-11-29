"""
dates module
Functions:
dates_between(date1, date2) -- return difference between
date1 and date2 in days
"""
from datetime import datetime


def dates_between(date1: str, date2: str) -> int:
    """
    Return difference between date1 and date2 in days
    :param date1: str
    :param date2: str
    :return: int
    """
    t_1 = datetime.strptime(date1, "%d.%m.%Y")
    t_2 = datetime.strptime(date2, "%d.%m.%Y")

    return (t_2 - t_1).days
