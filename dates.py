'''
Module
'''
from datetime import datetime


def dates_between(frst_dt: str, scnd_dt: str) -> int:
    '''
    frst_dt and scnd_dt must be in format "day.month.year"
    program calculate the difference between these dates in days
    :param frst_dt:
    :param scnd_dt:
    :return:
    '''
    first_date = datetime.strptime(frst_dt, "%d.%m.%Y")
    second_date = datetime.strptime(scnd_dt, "%d.%m.%Y")
    delta = second_date - first_date
    return delta.days
