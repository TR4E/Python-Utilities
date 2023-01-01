import time
from datetime import datetime

import pytz

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def getDateAndTime(timezone=None):
    if timezone is None:
        timezone = "Australia/Melbourne"

    date_and_time = str(datetime.now(getTimeZone(timezone))).split(" ")

    date = date_and_time[0]
    time = date_and_time[1].split(".")[0]

    return date + " " + time


def getDate(timezone=None):
    return getDateAndTime(timezone).split(" ")[0]


def getTime(timezone=None):
    return getDateAndTime(timezone).split(" ")[1]


def convertToMilliseconds(date_and_time):
    return int(datetime.strptime(date_and_time, DATE_TIME_FORMAT).timestamp() * 1000)


def getTimeZone(name):
    return pytz.timezone(name)


def getSystemTime():
    return round(time.time() * 1000)
