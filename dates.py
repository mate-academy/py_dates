"""module date"""
from datetime import datetime


def dates_between(frst_date: str, sec_date: str) -> int:
    """
    Calculate the difference between dates in days.
    Dates format should be DD.MM.YYYY
    :param frst_date: str
    :param sec_date: str
    :return: int
    """
    date_diff = datetime.strptime(sec_date, "%d.%m.%Y") - datetime.strptime(frst_date, "%d.%m.%Y")
    return abs(date_diff.days)
