r"""JSON Format classes for Python's `logging` module.

Availiable JSON Formatters:

- Advanced Json Format

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

- `Bunyan <https://github.com/trentm/node-bunyan>`_ Format

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

- Json Format

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

from .bunyan import BunyanFormat
from .simple import JsonFormat
from .advanced import AdvJsonFormat

__all__ = [
    "BunyanFormat",
    "JsonFormat",
    "AdvJsonFormat"
]
