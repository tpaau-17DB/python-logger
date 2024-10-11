"""
Python script for handling log formatting and filtering.

log_deb, log_inf, log_warn and log_err are used to print out messages in different formats.

VERBOSITY_LEVEL controlls which messages should be displayed and which should be discarded:
VERB=0 will display every log
VERB=1 will display all logs except debug ones
VERB=2 will display only warnings and errors
VERB<3 will display only errors

Passing override_prior=True to a function will display log ignoring It's priority.

"tabs" variable adds spacing at the beggining of a log.
One tab is equal to two spaces "  ", two tabs are four spaces etc.

GLOBAL_TABS works similarly to the tabs variable, but it affects all logs, not just the selected ones.

Logger will add date and time to all messages if PRINT_DATETIME is set to True (off by default).

DATETIME_FORMAT is the format in which datetime is printed.
"""

from datetime import datetime as dt

# Controlls which messages should be displayed
VERBOSITY_LEVEL = 2

# When set to True logger adds datetime to every message
PRINT_DATETIME = False

# The format in which datetime is printed
DATETIME_FORMAT = '%H:%M:%S'

# Adds spacing to all logs
GLOBAL_TABS = 0


# CONST VALUES
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[33m"
RED = "\033[91m"
EXT = "\033[0m"

# SETTERS
def set_global_tabs(value):
    """
    sets GLOBAL_TABS variable
    """
    if not isinstance(value, int):
        log_err(f"Expected int, got {type(value)}. Ignoring request.")
        return

    global GLOBAL_TABS
    GLOBAL_TABS = value


def set_datetime_format(value):
    """
    sets DATETIME_FORMAT
    """
    if not isinstance(value, str):
        log_err(f"Expected string, got {type(value)}. Ignoring request.")
        return

    global DATETIME_FORMAT
    DATETIME_FORMAT = value

def set_print_datetime(value):
    """
    sets PRINT_DATETIME
    """
    if not isinstance(value, bool):
        log_err(f"Expected boolean, got {type(value)}. Ignoring request.")
        return

    global PRINT_DATETIME
    PRINT_DATETIME = value


def set_verbosity(value):
    """
    sets the VERBOSITY_LEVEL
    """
    if not isinstance(value, int):
        log_err(f"Expected integer, got {type(value)}. Ignoring request.")
        return

    if value < 0 or value > 3:
        log_err("Failed to set verbosity! Value must be between 0 and 3.")
        return

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
    if VERBOSITY_LEVEL != 0 and not override_prior:
        return
    print(" " * 2 * (tabs + GLOBAL_TABS) + f"{BLUE}[DEB]{EXT} {_get_datetime()}{message}")

def log_inf(message, tabs=0, override_prior=False):
    """
    prints informative messages
    """
    if VERBOSITY_LEVEL > 1 and not override_prior:
        return
    print(" " * 2 * (tabs + GLOBAL_TABS) + f"{GREEN}[INF]{EXT} {_get_datetime()}{message}")

def log_warn(message, tabs=0, override_prior=False):
    """
    prints warnings
    """
    if VERBOSITY_LEVEL > 2 and not override_prior:
        return
    print(" " * 2 * (tabs + GLOBAL_TABS) + f"{YELLOW}[WAR]{EXT} {_get_datetime()}{message}")

def log_err(message, tabs=0, override_prior=False):
    """
    prints errors
    """
    if VERBOSITY_LEVEL > 3 and not override_prior:
        return
    print(" " * 2 * (tabs + GLOBAL_TABS) + f"{RED}[ERR]{EXT} {_get_datetime()}{message}")
