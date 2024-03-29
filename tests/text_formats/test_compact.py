"""Test cases for the Simple Text Formatter."""

import datetime
import logging
import re
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Union

import pytest

from pylogformats.text import CompactTextFormat


USE_DATETIME = datetime.datetime.utcnow()
RUSE_DATETIME = USE_DATETIME - datetime.timedelta(milliseconds=5)


@pytest.fixture
def log_record() -> logging.LogRecord:
    """Fixture for creating a log record to format."""
    record_data: Dict[str, Optional[Union[str, int]]] = {
        "name": "root",
        "levelno": 10,
        "pathname": "tests/json/bunyan.py",
        "lineno": 30,
        "msg": "A demo log message",
        "args": None,
    }
    record: logging.LogRecord = logging.makeLogRecord(record_data)
    record.__dict__["created"] = USE_DATETIME.timestamp()
    record.__dict__["relativeCreated"] = RUSE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"
    record.__dict__["function"] = "test_json"
    record.__dict__["levelname"] = "DEBUG"

    return record


@pytest.fixture
def args_log_record() -> logging.LogRecord:
    """Fixture for creating a log record to format."""
    record_data: Dict[str, Optional[Union[str, int, Tuple[str]]]] = {
        "name": "root",
        "levelno": 10,
        "pathname": "tests/json/bunyan.py",
        "lineno": 30,
        "msg": "A message with %s",
        "args": ("formatting",),
    }

    record: logging.LogRecord = logging.makeLogRecord(record_data)
    record.__dict__["created"] = USE_DATETIME.timestamp()
    record.__dict__["relativeCreated"] = RUSE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"
    record.__dict__["function"] = "test_json"
    record.__dict__["levelname"] = "DEBUG"

    return record


@pytest.fixture
def extra_log_record() -> logging.LogRecord:
    """Fixture for creating a log record to format."""
    record_data: Dict[str, Optional[Union[str, int]]] = {
        "name": "root",
        "levelno": 10,
        "pathname": "tests/json/bunyan.py",
        "lineno": 30,
        "msg": "A extra log message",
        "args": None,
    }

    record: logging.LogRecord = logging.makeLogRecord(record_data)
    record.__dict__["created"] = USE_DATETIME.timestamp()
    record.__dict__["relativeCreated"] = RUSE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"
    record.__dict__["function"] = "test_json"
    record.__dict__["levelname"] = "DEBUG"

    # Extras
    record.__dict__["str_extra"] = "Extra 1"
    record.__dict__["int_extra"] = 2
    record.__dict__["float_extra"] = 1.5

    return record


@pytest.fixture
def compact_formatter() -> logging.Formatter:
    """Fixture for creating a formatter class."""
    return CompactTextFormat()


def test_compact_correct_format(
    log_record: logging.LogRecord, compact_formatter: logging.Formatter
) -> None:
    """Test that the Compact Text formatter matches the regular expressions."""
    formatted_log: str = compact_formatter.format(log_record)

    assert (
        re.search(
            (
                r"\[[CEWID]{1} \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
                r" l:\w+ f:.+ ln:\d+\] .+[ ]{0,1}\[.+\]+"
            ),
            formatted_log,
        )
        is not None
    )


def test_compact_correct_values(
    log_record: logging.LogRecord, compact_formatter: logging.Formatter
) -> None:
    """Test that the Compact Text formatter values match the intended output."""
    formatted_log: str = compact_formatter.format(log_record)

    assert "D" == formatted_log[1]
    assert USE_DATETIME.strftime("%Y-%m-%d %H:%M:%S") in formatted_log
    assert "A demo log message" in formatted_log


def test_compact_with_args(
    args_log_record: logging.LogRecord, compact_formatter: logging.Formatter
) -> None:
    """Test that the Compact Formatter's message is properly formed with args."""
    formatted_log: str = compact_formatter.format(args_log_record)

    assert "A message with formatting" in formatted_log


def test_compact_with_extras(
    extra_log_record: logging.LogRecord, compact_formatter: logging.Formatter
) -> None:
    """Test that the Compact Text formatter contains extra information."""
    formatted_log: str = compact_formatter.format(extra_log_record)

    assert (
        re.search(
            (
                r"\[[CEWID]{1} \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
                r" l:\w+ f:.+ ln:\d+\] .+[ ]{0,1}\[.+\]+"
            ),
            formatted_log,
        )
        is not None
    )

    assert "[str_extra:Extra 1]" in formatted_log
    assert "[int_extra:2]" in formatted_log
    assert "[float_extra:1.5]" in formatted_log
