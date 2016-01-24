import datetime as dt

DEFAULT_DATE_FORMAT = "%Y-%m-%d"


def get_date(date_string, format_string=DEFAULT_DATE_FORMAT):
    return dt.datetime.strptime(date_string,format_string).date()


def format_date(date,format_string=DEFAULT_DATE_FORMAT):
    return dt.date.strftime(date,format_string)
