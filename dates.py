"""
docstring
"""
import datetime


def dates_between(date_one, date_two):
    """

    :param date_one:
    :param date_two:
    :return:
    """
    date_o = datetime.datetime.strptime(date_one, '%d.%m.%Y')
    date_t = datetime.datetime.strptime(date_two, '%d.%m.%Y')
    return (date_t - date_o).days
