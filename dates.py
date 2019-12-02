"""Calculate the difference between these dates in days."""
from datetime import datetime


def dates_between(date_one: str, date_two: str) -> int:
    """ Difference between two datetime objects"""
    date1 = datetime.strptime(date_one, "%d.%m.%Y")
    date2 = datetime.strptime(date_two, "%d.%m.%Y")
    return abs((date2 - date1).days)
