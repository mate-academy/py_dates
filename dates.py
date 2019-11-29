"""
This program calculates quantity of days btw 2 dates
"""
from datetime import datetime


def dates_between(date1: str, date2: str) -> int:
    """
    By means of imported module datetime calculate
    the days diff btw 2 dates
    :param date1: earlier date
    :param date2: later date
    :return: difference in days btw 2 dates
    """
    date_format = "%d.%m.%Y"
    days = str(datetime.strptime(date2, date_format) -
               datetime.strptime(date1, date_format)).split(" days")
    result = int(days[0])
    return result
