import dates


def test_millenium():
    assert dates. dates_between("01.01.2000", "29.11.2019") == 7272


def test_unixepoch():
    assert dates.dates_between("01.01.1970", "29.11.2019") == 18229


