"""A list of LogRecord internal attributes.

This is used to easily identify any additional attributes passed
in by a user using the `extra` key
"""

from typing import List


BASELINE: List[str] = [
    "args",
    "asctime",
    "created",
    "exc_info",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "message",
    "module",
    "msecs",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
]
