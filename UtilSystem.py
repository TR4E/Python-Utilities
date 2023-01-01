import multiprocessing
import threading

from apscheduler.schedulers.background import BackgroundScheduler


def startThread(function, args=None, joining=False):
    if args is None:
        args = []

    thread = threading.Thread(
        target=function,
        args=args
    )

    thread.start()

    if joining:
        thread.join()


def startProcess(function, args=None, joining=False):
    if args is None:
        args = []

    process = multiprocessing.Process(
        target=function,
        args=args
    )

    process.start()

    if joining:
        process.join()


def startSchedule(trigger, function, args=None, job_defaults=None):
    if args is None:
        args = []

    default_job_defaults = {
        "coalesce": False,
        "max_instances": 500,
        "misfire_grace_time": None
    }

    if job_defaults is not None:
        for (key, value) in job_defaults.items():
            default_job_defaults[key] = value

    scheduler = BackgroundScheduler(job_defaults=job_defaults)

    scheduler.add_job(
        trigger=trigger,
        executors=None,
        func=function,
        args=args
    )

    scheduler.start()
