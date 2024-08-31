"""
Logger script for handling log formatting and filtering

log_deb, log_mess, log_warn and log_err are used to
print out messages in different formats

VERBOSITY_LEVEL filters logs based on their importance:
    -all logs for 0
    -all logs except debug ones for 1
    -only warnings and errors for 2 (default)
    -only errors will be displayed for 3
    -values greater than 3 mute all logs (quiet mode)

Passing override_prior=True to a function will print the message ignoring It's priority



Logger will add date and time to all messages if PRINT_DATETIME is set to true.

DATETIME_FORMAT determines the format in which datetime is printed
"""

from datetime import datetime as dt

# Controlls log filtering
VERBOSITY_LEVEL = 2

# When set to true datetime will be added to every message
PRINT_DATETIME = True

# The format in which datetime is printed
DATETIME_FORMAT = '%H:%M:%S'

# CONST VALUES
BLUE = "\033[34m"
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


# INTERNAL FUNCTIONS
def _get_datetime():
    """
    Returns current, formatted datetime
    """
    if PRINT_DATETIME:
        return f"[{dt.now().strftime(DATETIME_FORMAT)}] "
    return ""


# METHODS
def log_deb(message, tabs=0, override_prior=False):
    """
    used to print out debug info
    """
    if VERBOSITY_LEVEL > 0 and not override_prior:
        return
    print(" " * 2 * tabs + f"{BLUE}[DEB]{EXT} {_get_datetime()}{message}")


def log_mess(message, tabs=0, override_prior=False):
    """
    prints standard, informative logs
    """
    if VERBOSITY_LEVEL > 1 and not override_prior:
        return
    print(" " * 2 * tabs + f"{GREEN}[LOG]{EXT} {_get_datetime()}{message}")


def log_warn(message, tabs=0, override_prior=False):
    """
    prints warnings
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
    print(" " * 2 * tabs + f"{RED}[ERR]{EXT}{_get_datetime()}{message}")
