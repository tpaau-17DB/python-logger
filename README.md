# python-logger

git repo: https://github.com/tpaau-17DB/python-logger

Python script for handling log formatting and filtering.

## Installing

To download git repo you can run:

```
git clone https://github.com/tpaau-17DB/python-logger.git
```

Go to the downloaded repo with:

```
cd python-logger
```

And finally install the package with pip:

```
pip install .
```

## Running

You can test if the script is installed correctly by running this python script:

```
import logger as l

l.set_verbosity(0)

l.log_deb("This is a debug log")
l.log_inf("This is a message", 1)
l.log_warn("This is a warning", 2)
l.log_err("This is an error", 3)
```
