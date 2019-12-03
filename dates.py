"""Calculating the difference between dates in days"""
import datetime
import numpy


def dates_between(first_date: str, second_date: str) -> int:
    """
    Calculating the difference between dates in days
    :param first_date: data in string
    :param second_date: data in string
    :return: difference between first and second dates
    """
    date1 = datetime.datetime.strptime(first_date, '%d.%m.%Y')
    date2 = datetime.datetime.strptime(second_date, '%d.%m.%Y')
    diff = datetime.timedelta()
    diff = date1 - date2
    return diff.days
