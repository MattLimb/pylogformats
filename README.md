# pyLogFormats

A collection of Logging Formats for the Pyton Standard Logger. Thats it. 

Right now, this is a fairly small list, however there are a few log formats that I'd like to add. Checkout the Future Additions Section below. 

[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Formats Included:

- BunyanFormat (https://github.com/trentm/node-bunyan)
```json
{
    "time": "2021-02-04T23:01:00.781Z", 
    "name": "root", 
    "pid": 15504, 
    "level": 40, 
    "msg": "TEST", 
    "hostname": "Sophie", 
    "v": 0
}
```
- JSONFormat 
```json
{
    "logger": "root", 
    "timestamp": "2021-02-04T23:01:46.435011",
    "message": "TEST",
    "level": "ERROR",
    "levelno": 40,
    "function": "<module>",
    "process": {
        "number": 13316,
        "name": "MainProcess"
    },
    "thread": {
        "number": 10704, 
        "name": "MainThread"
    }, 
    "v": 1
}
```
- AdvJSONFormat (For Verbose JSON Logging)
```json
{
    "logger": "root",
    "timestamp": "2021-02-04T23:02:52.522958",
    "rtimestamp": "2021-02-04T23:02:37.518800",
    "message": "TEST",
    "level": "ERROR", 
    "levelno": 40,
    "location": {
        "pathname": "<FULL_PATH>\\test_logger.py", 
        "module": "test_logger", 
        "filename": "test_logger.py", 
        "function": "<module>", 
        "line": 16
    }, 
    "process": {
        "number": 2300, 
        "name": "MainProcess"
    }, 
    "thread": {
        "number": 12516,
        "name": "MainThread"
    }, 
    "v": 1
}
```


## Installation 

Clone the git repo

```sh
git clone git@github.com:MattLimb/pylogformats.git
```

Install 

```sh
python3 -m pip install pylogformats
```

## Usage

Use the formatter as you would any other Python Formatter:

```python
import pylogformat 
import logging
import sys

logger = logging.getLogger()

logHandler = logging.StreamHandler(sys.stdout)

formatter = pylogformat.AdvJSONFormat()
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.setLevel(logging.DEBUG)
```

You can also use `dictConfig`:

```python
LOG_CONFIG = {
  'formatters': {
    'jsonformatter': {
      '()' : 'pylogformats.JSONFormat'
    }
  },
  'handlers': {
    'debug': {
      'class': 'logging.StreamHandler',
      'formatter': 'jsonformatter',
      'stream': 'ext://sys.stdout'
    },
  },

  'root': {
    'level': 'DEBUG',
    'handlers': ['debug']
  },
  'version': 1
}

import logging.config

logging.config.dictConfig(LOG_CONFIG)
```

