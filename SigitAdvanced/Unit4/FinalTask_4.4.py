def gen_secs():
    """
    Generator function that yields all possible seconds in a minute (0-59).
    """
    for sec in range(60):
        yield sec

def gen_minutes():
    """
    Generator function that yields all possible minutes in an hour (0-59).
    """
    for minute in range(60):
        yield minute

def gen_hours():
    """
    Generator function that yields all possible hours in a day (0-23).
    """
    for hour in range(24):
        yield hour

def gen_time():
    """
    Generator function that yields all possible times in a day in the format 'HH:MM:SS'.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)

def gen_years(start=2019):
    """
    Generator function that yields all years starting from the given start year.
    Args:
        start (int): The starting year (default is 2019).
    """
    year = start
    while True:
        yield year
        year += 1

def gen_months():
    """
    Generator function that yields all months in a year (1-12).
    """
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    """
    Generator function that yields all days in a given month, taking into account leap years.
    Args:
        month (int): The month number (1-12).
        leap_year (bool): Whether the year is a leap year or not (default is True).
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and leap_year:
        num_days = 29
    else:
        num_days = days_in_month[month - 1]
    for day in range(1, num_days + 1):
        yield day

def gen_date():
    """
    Generator function that yields all possible dates and times in the format 'DD/MM/YYYY HH:MM:SS'.
    """
    for year in gen_years():
        leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)



def main():
    date_gen = gen_date()

    for i in range(1000000):
        next(date_gen)
    print(next(date_gen))  # Print the 1,000,001st date

    for i in range(1000000):
        next(date_gen)
    print(next(date_gen))  # Print the 2,000,001st date

    for i in range(1000000):
        next(date_gen)
    print(next(date_gen))  # Print the 3,000,001st date

if __name__ == "__main__":
    main()