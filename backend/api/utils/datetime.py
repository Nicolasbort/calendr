from datetime import date, datetime, time, timedelta


def diff(time_start: time, time_end: time) -> int:
    """
    Time difference in minutes
    """
    datetime_end = datetime.combine(date.today(), time_end)
    datetime_start = datetime.combine(date.today(), time_start)

    diff = datetime_end - datetime_start

    return round(diff.total_seconds() / 60)


def add_minutes_to_time(time: time, minutes: int) -> time:
    """
    Add minutes to a time object
    """
    delta = timedelta(minutes=minutes)

    start = datetime(2000, 1, 1, hour=time.hour, minute=time.minute, second=time.second)
    end = start + delta

    return end.time()
