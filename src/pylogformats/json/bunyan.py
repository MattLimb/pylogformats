"""Bunyan JSON Format."""

import json
import logging
import platform
from datetime import datetime
from typing import Any
from typing import Dict
from typing import Optional

from pylogformats.baseline import BASELINE


class BunyanFormat(logging.Formatter):
    """A Simple Bunyan JSON Formatter.

    Extends the `logging.Formatter` class to correctly format a log record as bunyan.

    Example Usage:

    >>> import logging
    >>> import sys
    >>> import pylogformats
    >>>
    >>> # Setup the Stream Handler Using Bunyan
    >>> stream_handler = logging.StreamHandler(sys.stdout)
    >>> stream_handler.setFormatter(pylogformats.BunyanFormat())
    >>>
    >>> # Setup the logging config using the stream hander and the DEBUG logging level
    >>> logging.basicConfig(handlers=[stream_handler], level=logging.DEBUG)
    >>>
    >>> # The test log
    >>> logging.debug("Test Log")
    {"time": ..., "name": "root", "pid": ..., "level": 10, "msg": "Test Log", \
"hostname": ..., "v": 0}
    >>>
    >>> logging.debug(
    ...     "Test Log With Extra",
    ...     extra={
    ...         "whatami": "An Extra"
    ...     }
    ... )
    {"time": ..., "name": "root", "pid": ..., "level": 10, "msg": "Test Log \
With Extra", "hostname": ..., "v": 0, "whatami": "An Extra"}
    >>> # Clean up Logging
    >>> logging.getLogger().removeHandler(stream_handler)

    In some lines of the example code, there is an output of a sample log.
    This log shows some values as an ellipsis (...). This is because it is a Doctest
    codeblock which helps ensure code examples are up-to-date when code changes.

    Please be assured that these ellipsis are not present when formatting the log
    and the keys that use them will have real, accurate values in them.

    """

    # Following line ignores Flake8 because this overrides a pre-existing
    # function which is formatted using CamelCase instead of the PEP8 approved
    # snake case. This allows it to comply with the logging.LogFormatter subclass.
    def formatTime(  # noqa: N802
        self, record: logging.LogRecord, datefmt: Optional[str] = None
    ) -> str:
        """Format LogRecord Times into the correct formatted string String.

        :param record: An instance of *logging.LogRecord* which contains all relevant \
information about the event being logged.
        :type record: logging.LogRecord
        :param datefmt: A valid `datetime.strftime()` format string.
        :type datefmt: str | None
        :return: A string representation of the Bunyan formatted logging event.
        :rtype: str
        """
        if datefmt is None:
            datefmt = "%Y-%m-%dT%H:%M:%S.%f"

        created_timestamp: float = record.created
        created_datetime: datetime = datetime.fromtimestamp(created_timestamp)

        return created_datetime.strftime(datefmt)

    def format(self, record: logging.LogRecord) -> str:
        """Format LogRecords into a Bunyan JSON String.

        :param record: An instance of *logging.LogRecord* which contains all relevant \
information about the event being logged.
        :type record: logging.LogRecord
        :return: A string representation of the Bunyan formatted logging event.
        :rtype: str
        """
        formatted_message: str = record.getMessage()

        formatted_record: Dict[str, Any] = {
            "time": (self.formatTime(record, "%Y-%m-%dT%H:%M:%S.%f"))[:-3] + "Z",
            "name": record.name,
            "pid": record.process or 0,
            "level": record.levelno or 0,
            "msg": formatted_message,
            "hostname": platform.node(),
            "v": 0,
        }

        for key, value in vars(record).items():
            if key not in BASELINE:
                formatted_record[key] = value

        return json.dumps(formatted_record)
