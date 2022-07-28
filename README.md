# PyLogFormats

[![PyPI](https://img.shields.io/pypi/v/pylogformats.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/pylogformats.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/pylogformats)][python version]
[![License](https://img.shields.io/pypi/l/pylogformats)][license]

[![Read the documentation at https://pylogformats.readthedocs.io/](https://img.shields.io/readthedocs/pylogformats/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/MattLimb/pylogformats/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/MattLimb/pylogformats/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/pylogformats/
[status]: https://pypi.org/project/pylogformats/
[python version]: https://pypi.org/project/pylogformats
[read the docs]: https://pylogformats.readthedocs.io/
[tests]: https://github.com/MattLimb/pylogformats/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/MattLimb/pylogformats
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

- Json Formatters
  - AdvJsonFormat
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
  - BunyanFormat
  ```json
  {
    "time": "2021-02-04T23:01:00.781Z",
    "name": "root",
    "pid": 15504,
    "level": 40,
    "msg": "TEST",
    "hostname": "HerculesPC",
    "v": 0
  }
  ```
  - JsonFormat
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
- Text Formatters

  - SimpleTextFormat

  ```text
  [DEBUG] [2021-02-04 23:01:46] A Test Debug Log
  ```

  - CompactTextFormat

  ```text
  [D 2021-02-04 23:01:46 l:root f:<module> ln:5] A Test Log [includesExtras:Yes]
  ```

## Installation

You can install _PyLogFormats_ via [pip] from [PyPI]:

```console
$ pip install pylogformats
```

## Usage

For an explanation of this, and more usage instructions please visit the [documentation](https://pylogformats.readthedocs.io/usage.html)

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

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_PyLogFormats_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/MattLimb/pylogformats/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/MattLimb/pylogformats/blob/main/LICENSE
[contributor guide]: https://github.com/MattLimb/pylogformats/blob/main/CONTRIBUTING.md
