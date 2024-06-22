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
"""

#Controlls which messages should be displayed
VERBOSITY_LEVEL = 1

def set_verbosity(val):
    """
    sets the verbosity level
    """
    global VERBOSITY_LEVEL;
    VERBOSITY_LEVEL = val

def get_verbosity():
    """
    returns verbosity value
    """
    return VERBOSITY_LEVEL

def log_mess(message, layer = 0):
    """
    prints messages in log format
    """
    if VERBOSITY_LEVEL > 0:
        return
    print(" " * 2 * layer + f"\033[92m[LOG]\033[0m {message}")


def log_warn(message, layer = 0):
    """
    prints messages in warning format
    """
    if VERBOSITY_LEVEL > 1:
        return
    print(" " * 2 * layer + f"\033[33m[WARN]\033[0m {message}")


def log_err(message, layer = 0):
    """
    prints messages in error format
    """
    if VERBOSITY_LEVEL > 2:
        return
    print(" " * 2 * layer + f"\033[91m[ERR]\033[0m {message}")
