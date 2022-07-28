"""Compact Text Format."""

import logging

from pylogformats.baseline import BASELINE


class CompactTextFormat(logging.Formatter):
    """A formatter for an opinionated Compact Text format.

    Extends the `logging.Formatter` class to correctly format a log record using
    this format.

    Example Usage:

    >>> import logging
    >>> import sys
    >>> import pylogformats
    >>>
    >>> # Setup the Stream Handler Using JsonFormat
    >>> stream_handler = logging.StreamHandler(sys.stdout)
    >>> stream_handler.setFormatter(pylogformats.CompactTextFormat())
    >>>
    >>> # Setup the logging config using the stream hander and the DEBUG logging level
    >>> logging.basicConfig(handlers=[stream_handler], level=logging.DEBUG)
    >>>
    >>> # The test log
    >>> logging.debug("Test Log")
    [D ... ... l:root f:... ln:...] Test Log
    >>>
    >>> logging.debug(
    ...     "Test Log With Extra",
    ...     extra={"whatami": "An Extra"}
    ... )
    [D ... ... l:root f:... ln:...] Test Log With Extra [whatami:An Extra]
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
        log_level: str = record.levelname[0].upper()
        date_str: str = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        preamble: str = (
            f"[{log_level} {date_str} l:{record.name} f:{record.filename or 'unknown'} "
            f"ln:{record.lineno}]"
        )

        extras: str = " ".join([
            f"[{key}:{value}]"
            for key, value in vars(record).items()
            if key not in BASELINE
        ])

        return f"{preamble} {record.getMessage()} {extras}"
