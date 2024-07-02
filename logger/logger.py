"""
Logger script that can be used to debug or in final project

log_mess prints message in '[LOG] <message>' format
the same applies for log_warn and log_err, but [LOG]
is replaced by [WARN] and [ERR] respectively

VERBOSITY_LEVEL controlls which messages should be
displayed and which should be discarded

VERB=0 will display every log
VERB=1 will display only warnings and errors
VERB<2 will display only errors

Passing override_prior=True to a function will print log
no matter its priority

Logger will add date and time to all messages if
PRINT_DATETIME is set to true.

DATETIME_FORMAT determines in what format should date be displayed
"""

from datetime import datetime as dt

#Controlls which messages should be displayed
VERBOSITY_LEVEL = 1

#When set to true logger adds datetime to every message
PRINT_DATETIME = True

#The format in which datetime is printed
DATETIME_FORMAT = '%H:%M:%S'


def set_datetime_format(value):
    """
    sets DATETIME_FORMAT
    """
    global DATETIME_FORMAT
    DATETIME_FORMAT = value


def set_print_datetime(value):
    """
    sets PRINT_DATETIME
    """
    global PRINT_DATETIME
    PRINT_DATETIME = value


def set_verbosity(value):
    """
    sets the verbosity level
    """
    global VERBOSITY_LEVEL
    VERBOSITY_LEVEL = value


def get_datetime_format():
    """
    returns DATETIME_FORMAT
    """
    return DATETIME_FORMAT


def get_verbosity():
    """
    returns verbosity value
    """
    return VERBOSITY_LEVEL


def _get_datetime():
    """
    Returns datetime in printable format
    """
    if PRINT_DATETIME:
        return f"[{dt.now().strftime(DATETIME_FORMAT)}] "
    return ""

def log_mess(message, layer=0, override_prior=False):
    """
    prints messages in log format
    """
    if VERBOSITY_LEVEL > 0 and not override_prior:
        return
    print(" " * 2 * layer + f"\033[92m[LOG]\033[0m {_get_datetime()}{message}")


def log_warn(message, layer=0, override_prior=False):
    """
    prints messages in warning format
    """
    if VERBOSITY_LEVEL > 1 and not override_prior:
        return
    print(" " * 2 * layer + f"\033[33m[WARN]\033[0m {_get_datetime()}{message}")


def log_err(message, layer=0, override_prior=False):
    """
    prints messages in error format
    """
    if VERBOSITY_LEVEL > 2 and not override_prior:
        return
    print(" " * 2 * layer + f"\033[91m[ERR]\033[0m {_get_datetime()}{message}")
