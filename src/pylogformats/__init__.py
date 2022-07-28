r"""Easy to Use Formatter Classes for the Python `logging` module.

Availiable JSON Formatters:

- `Advanced Json Format <#pylogformats.AdvJsonFormat>`_

.. code-block:: json
    :caption: Example Advanced Json Log
    :linenos:
    :lineno-start: 1
    :name: adv-json-format

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

- `Bunyan Format <#pylogformats.BunyanFormat>`_

`Bunyan Specification <https://github.com/trentm/node-bunyan>`_

.. code-block:: json
    :caption: Example Bunyan Json Log
    :linenos:
    :lineno-start: 1
    :name: bunyan-json-format

    {
        "time": "2021-02-04T23:01:00.781Z",
        "name": "root",
        "pid": 15504,
        "level": 40,
        "msg": "TEST",
        "hostname": "HerculesPC",
        "v": 0
    }

- `Json Format <#pylogformats.JsonFormat>`_

.. code-block:: json
    :caption: Example Json Log
    :linenos:
    :lineno-start: 1
    :name: json-format

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

"""

from . import json
from . import text
from .json import AdvJsonFormat
from .json import BunyanFormat
from .json import JsonFormat
from .text import CompactTextFormat
from .text import SimpleTextFormat


# Legacy Aliases

JSONFormat = JsonFormat
AdvJSONFormat = AdvJsonFormat

__all__ = [
    # Json Formats
    "AdvJsonFormat",
    "BunyanFormat",
    "JsonFormat",
    "JSONFormat",
    "AdvJSONFormat",
    # Text Formats
    "CompactTextFormat",
    "SimpleTextFormat",
    # Additonal Module Imports
    "json",
    "text",
]
