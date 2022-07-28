"""Standard JSON Format."""

import json
import logging
from datetime import datetime
from typing import Any
from typing import Dict

from pylogformats.baseline import BASELINE


class JsonFormat(logging.Formatter):
    """A formatter for an opinionated Json format.

    Extends the `logging.Formatter` class to correctly format a log record using
    this format.

    Example Usage:

    >>> import logging
    >>> import sys
    >>> import pylogformats
    >>>
    >>> # Setup the Stream Handler Using JsonFormat
    >>> stream_handler = logging.StreamHandler(sys.stdout)
    >>> stream_handler.setFormatter(pylogformats.JsonFormat())
    >>>
    >>> # Setup the logging config using the stream hander and the DEBUG logging level
    >>> logging.basicConfig(handlers=[stream_handler], level=logging.DEBUG)
    >>>
    >>> # The test log
    >>> logging.debug("Test Log")
    {"logger": "root", "timestamp": ..., "message": "Test Log", "level": "DEBUG", \
"levelno": 10, "function": "<module>", "process": {"number": ..., "name": \
"MainProcess"}, "thread": {"number": ..., "name": "MainThread"}, "v": 1}
    >>>
    >>> logging.debug(
    ...     "Test Log With Extra",
    ...     extra={"whatami": "An Extra"}
    ... )
    {"logger": "root", "timestamp": ..., "message": "Test Log With Extra", \
"level": "DEBUG", "levelno": 10, "function": "<module>", "process": {\
"number": ..., "name": "MainProcess"}, "thread": {"number": ..., "name": \
"MainThread"}, "v": 1, "whatami": "An Extra"}
    >>> # Clean up Logging
    >>> logging.getLogger().removeHandler(stream_handler)

    In some lines of the example code, there is an output of a sample log.
    This log shows some values as an ellipsis (...). This is because it is a Doctest
    codeblock which helps ensure code examples are up-to-date when code changes.

    Please be assured that these ellipsis are not present when formatting the log
    and the keys that use them will have real, accurate values in them.

    """

    def format(self, record: logging.LogRecord) -> str:
        """Format LogRecords into an simplified JSON log format.

        :param record: An instance of *logging.LogRecord* which contains all relevant \
information about the event being logged.
        :type record: logging.LogRecord
        :return: A string representation of the Bunyan formatted logging event.
        :rtype: str
        """
        formatted_message: Dict[str, Any] = {
            "logger": record.name,
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "message": record.getMessage(),
            "level": record.levelname,
            "levelno": record.levelno,
            "function": record.funcName,
            "process": {
                "number": record.process or 0,
                "name": record.processName or "unknown",
            },
            "thread": {
                "number": record.thread or 0,
                "name": record.threadName or "unknown",
            },
            "v": 1,
        }

        for key, value in vars(record).items():
            if key not in BASELINE:
                formatted_message[key] = value

        return json.dumps(formatted_message)
