# python-logger

git repo: https://github.com/mikolajArchUser/python-logger

Python logger package that can be used to debug or in the finished project.

## Installing

To download git repo you can run:

```
git clone https://github.com/mikolajArchUser/python-logger
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

You can test if the script is installed correctly by running this script:

```
import logger as l

l.set_verbosity(0)

l.log_mess("This is a message")
l.log_warn("This is a warning", 1)
l.log_err("This is an error", 2)
```
