"""
Python script for handling log formatting and filtering.

log_deb, log_mess, log_warn and log_err are used to print out messages in different formats.

VERBOSITY_LEVEL controlls which messages should be displayed and which should be discarded.
VERB=0 will display every log
VERB=1 will display only warnings and errors
VERB<2 will display only errors

Passing override_prior=True to a function will display log ignoring It's priority.

"tabs" variable adds spacing at the beggining of a log.
One tab is equal to two spaces "  ", two tabs are four spaces etc.

Logger will add date and time to all messages if PRINT_DATETIME is set to True (off by default).

DATETIME_FORMAT is the format in which datetime is printed
"""

from datetime import datetime as dt

#Controlls which messages should be displayed
VERBOSITY_LEVEL = 2

#When set to True logger adds datetime to every message
PRINT_DATETIME = False

#The format in which datetime is printed
DATETIME_FORMAT = '%H:%M:%S'


# CONST VALUES
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[33m"
RED = "\033[91m"
EXT = "\033[0m"

# SETTERS
def set_datetime_format(value):
    """
    sets DATETIME_FORMAT
    """
    global DATETIME_FORMAT

    try:
        dt.now().strftime(value)
    except ValueError:
        log_err(f"Datetime format '{value}' is incorrect. Ignoring request.")
        return

    DATETIME_FORMAT = value


def set_print_datetime(value):
    """
    sets PRINT_DATETIME
    """
    global PRINT_DATETIME
    PRINT_DATETIME = value
    if isinstance(value, bool):
        PRINT_DATETIME = value
    else:
        log_err(f"Expected boolean, got {type(value)}. Ignoring request.")

def set_verbosity(value):
    """
    sets the VERBOSITY_LEVEL
    """
    global VERBOSITY_LEVEL
    if isinstance(value, int):
        VERBOSITY_LEVEL = value
    else:
        log_err(f"Expected integer, got {type(value)}. Ignoring request.")


# GETTERS
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


# INTERNAL METHODS
def _get_datetime():
    """
    Returns datetime in printable format
    """
    if PRINT_DATETIME:
        return f"[{dt.now().strftime(DATETIME_FORMAT)}] "
    return ""


# LOG METHODS
def log_deb(message, tabs=0, override_prior=False):
    """
    Used to print debug info
    """
    if VERBOSITY_LEVEL > 0 and not override_prior:
        return
    print(" " * 2 * tabs + f"{BLUE}[DEB]{EXT} {_get_datetime()}{message}")


def log_mess(message, tabs=0, override_prior=False):
    """
    prints messages
    """
    if VERBOSITY_LEVEL > 1 and not override_prior:
        return
    print(" " * 2 * tabs + f"{GREEN}[LOG]{EXT} {_get_datetime()}{message}")


def log_warn(message, tabs=0, override_prior=False):
    """
    prints warings
    """
    if VERBOSITY_LEVEL > 2 and not override_prior:
        return
    print(" " * 2 * tabs + f"{YELLOW}[WARN]{EXT} {_get_datetime()}{message}")


def log_err(message, tabs=0, override_prior=False):
    """
    prints errors
    """
    if VERBOSITY_LEVEL > 3 and not override_prior:
        return
    print(" " * 2 * tabs + f"{RED}[ERR]{EXT} {_get_datetime()}{message}")
