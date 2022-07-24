# Usage

_PyLogFormats_ is intended to be used by Python's built-in logging framework called `logging`.

To learn more about `logging`: [https://docs.python.org/3/library/logging.html](https://docs.python.org/3/library/logging.html)

This page will show you how to use the `logging` formatters provided by _PyLogFormats_.

The guides provided here uses `JsonFormatter` however any formatter provided by _PyLogFormats_ will work in its place.

## Using `logging.basicConfig()`

1. Create the logging handler to be formatted.

```python
handler = logging.StreamHandler(sys.stdout)
```

Any handler Python `logging` provides will work here. See [this page](https://docs.python.org/3/howto/logging.html#useful-handlers) for a list of Python `logging` handlers.

2. Set the formatter class to be used by this logging handler.

```python
handler.setFormatter(JsonFormat())
```

3. Now we can call `logging.basicConfig` to set everything up.

```python
logging.basicConfig(handlers=[handler], level=logging.DEBUG)
```

Any Logging level can be used here. `logging.DEBUG` is used here for demonstrative purposes. See [this page](https://docs.python.org/3/howto/logging.html#logging-levels) to learn more about Python's logging levels.

4. Now one of the logging functions Python provides can be used to use the new formatter.

```python
logging.critical("Critical Log")
logging.error("Error Log")
logging.warning("Warning Log")
logging.info("Info Log")
logging.debug("Debug Log")
```

### Full Example

```py
import logging
import sys

from pylogformats import JsonFormat

# Create the logging handler
handler = logging.StreamHandler(sys.stdout)

# Add the formatter class to the handler we just created.
handler.setFormatter(JsonFormat())

# Use basicConfig to setup the loggers.
logging.basicConfig(handlers=[handler], level=logging.DEBUG)

# Use the normal logging methods to see formatted logs in your terminal
logging.critical("Critical Log")
logging.error("Error Log")
logging.warning("Warning Log")
logging.info("Info Log")
logging.debug("Debug Log")

```

## Using `logging.dictConfig()`

`logging.dictConfig()` is an advanced method for setting up `logging`. As such, only and example is given here. For explainations about how this works, please visit the `logging` documentation here: [https://docs.python.org/3/library/logging.config.html](https://docs.python.org/3/library/logging.config.html)

```python

import logging.config

LOG_CONFIG = {
  'formatters': {
    'jsonformatter': {
      '()' : 'pylogformats.JsonFormat'
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


logging.config.dictConfig(LOG_CONFIG)
```
