"""
You have two dates in the format DD.MM.YYYY.
Calculate the difference between these dates in days.
"""

import datetime


def dates_between(date1, date2) -> int:
    """Calculate the difference"""
    date1 = datetime.datetime.strptime(str(date1), '%d.%m.%Y')
    date2 = datetime.datetime.strptime(date2, '%d.%m.%Y')
    return (date2 - date1).days
