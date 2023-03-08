from datetime import date, datetime, time


def diff(time_start: time, time_end: time):
    """
    Time in minutes
    """
    datetime_end = datetime.combine(date.today(), time_end)
    datetime_start = datetime.combine(date.today(), time_start)

    diff = datetime_end - datetime_start

    return round(diff.total_seconds() / 60)
