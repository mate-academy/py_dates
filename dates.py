"""docstring"""
from datetime import datetime


def dates_between(date1: str, date2: str) -> int:
    """return difference between two date in days"""
    return (datetime.strptime(date2, "%d.%m.%Y")
            - datetime.strptime(date1, "%d.%m.%Y")).days
