"""delta time module"""
import datetime


def dates_between(firstdate: str, seconddate: str) -> int:
    """
    secondate - firstdate in format "%d.%m.%Y"
    :param firstdate:
    :param seconddate:
    :return: different in days
    """
    firstdatef = datetime.datetime.strptime(firstdate, "%d.%m.%Y")
    seconddatef = datetime.datetime.strptime(seconddate, "%d.%m.%Y")
    result = seconddatef-firstdatef
    return result.days
