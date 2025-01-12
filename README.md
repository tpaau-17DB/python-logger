# python-logger

Python script for handling log formatting and filtering.


## Installing
To install the package, run:
```
pip install .
```


## Running

You can test if the script is installed correctly by running this script:

```
import logger as l

l.set_verbosity(0)

l.log_deb("This is a debug log")
l.log_inf("This is a message", 1)
l.log_warn("This is a warning", 2)
l.log_err("This is an error", 3)
```
