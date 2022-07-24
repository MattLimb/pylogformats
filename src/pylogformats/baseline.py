"""A list of LogRecord internal attributes.

This is used to easily identify any additional attributes passed
in by a user using the `extra` key
"""

import logging
from typing import List


_LOG_RECORD: logging.LogRecord = logging.makeLogRecord(
    {
        "name": "root",
        "level": 10,
        "pathname": "tests/json/bunyan.py",
        "lineno": 30,
        "msg": "A demo log message",
        "args": None,
    }
)

BASELINE: List[str] = list(_LOG_RECORD.__dict__.keys())
