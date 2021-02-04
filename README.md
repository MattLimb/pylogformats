# pyLogFormats

A collection of Logging Formats for the Pyton Standard Logger. Thats it. 

Right now, this is a fairly small list, however there are a few log formats that I'd like to add. Checkout the Future Additions Section below. 

[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Formats Included:

- BunyanFormat (https://github.com/trentm/node-bunyan)
- JSONFormat 
- AdvJSONFormat (For Verbose JSON Logging)

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

formatter = AdvJSONFormat()
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

