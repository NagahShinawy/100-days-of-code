# get quarter of mon

FEB = 2


def get_quarter_by_month(month: int):
    """
    retreive the quarter of a month. ex: Jan is in Q1, April in Q2, ect
    :param month: valid int month
    :return: quarter that belongs to that month
    """
    if month not in range(1, 13):
        raise ValueError(f"invalid month <{month}>")
    if month in range(1, 4):
        return "Q1"
    if month in range(4, 7):
        return "Q2"
    if month in range(7, 10):
        return "Q3"
    return "Q4"


for mon in range(1, 13):
    print(mon, get_quarter_by_month(mon))


print("#" * 50)


def is_leap_year(year):
    """
    check if the year is leap or not
    :param year: year in geo
    :return: True if the year is leap otherwise False
    """
    if year % 4 == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                # print("{0} is a leap year".format(year))
                return True
            else:
                # print("{0} is not a leap year".format(year))
                return False
        else:
            return True
            # print("{0} is a leap year".format(year))
    else:
        return False
        # print("{0} is not a leap year".format(year))


def days_in_month(year, month):
    """
    get how many days in month in a year
    :param year: year as int
    :param month: valid month
    :return: number of days in a month. if year is leap then Feb is 29 days
    """
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month <{month}>")
    month_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if is_leap_year(year=year):
        month_days[FEB] = 29
    return month_days[month]


print(days_in_month(year=2000, month=3))
print(days_in_month(year=2000, month=2))
print(days_in_month(year=2022, month=12))
print(days_in_month(year=2022, month=13))
