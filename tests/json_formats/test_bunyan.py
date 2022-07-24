"""Test cases for the Bunyan Formatter."""

import logging
import json
import datetime
import re
from typing import Dict, Optional, Union, Tuple

import pytest

from pylogformats.json import BunyanFormat

USE_DATETIME = datetime.datetime.utcnow()


@pytest.fixture
def log_record() -> logging.LogRecord:
    """Fixture for creating a log record to format."""
    record_data: Dict[str, Optional[Union[str, int]]] = {
        "name": "root",
        "level": 10,
        "pathname": "tests/json/bunyan.py",
        "lineno": 30,
        "msg": "A demo log message",
        "args": None,
    }
    record: logging.LogRecord = logging.makeLogRecord(record_data)
    record.__dict__["created"] = USE_DATETIME.timestamp()
    record.__dict__["relativeCreated"] = USE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"

    return record


@pytest.fixture
def args_log_record() -> logging.LogRecord:
    """Fixture for creating a log record to format."""
    record_data: Dict[str, Optional[Union[str, int, Tuple[str]]]] = {
        "name": "root",
        "level": 10,
        "pathname": "tests/json/bunyan.py",
        "lineno": 30,
        "msg": "A message with %s",
        "args": ("formatting",),
    }

    record: logging.LogRecord = logging.makeLogRecord(record_data)
    record.__dict__["created"] = USE_DATETIME.timestamp()
    record.__dict__["relativeCreated"] = USE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"

    return record


@pytest.fixture
def extra_log_record() -> logging.LogRecord:
    """Fixture for creating a log record to format."""
    record_data: Dict[str, Optional[Union[str, int]]] = {
        "name": "root",
        "level": 10,
        "pathname": "tests/json/bunyan.py",
        "lineno": 30,
        "msg": "A extra log message",
        "args": None,
    }

    record: logging.LogRecord = logging.makeLogRecord(record_data)
    record.__dict__["created"] = USE_DATETIME.timestamp()
    record.__dict__["relativeCreated"] = USE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"

    # Extras
    record.__dict__["str_extra"] = "Extra 1"
    record.__dict__["int_extra"] = 2
    record.__dict__["float_extra"] = 1.5

    return record


@pytest.fixture
def bunyan_formatter() -> logging.Formatter:
    """Fixture for creating a formatter class."""
    return BunyanFormat()


def test_bunyan_correct_keys(
    log_record: logging.LogRecord, bunyan_formatter: logging.Formatter
) -> None:
    """Test that the bunyan formatter contains all relevant keys."""
    formatted_log: str = bunyan_formatter.format(log_record)

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, object] = json.loads(formatted_log)

    # Ensure all required keys are present
    assert "time" in valid_json
    assert "name" in valid_json
    assert "pid" in valid_json
    assert "level" in valid_json
    assert "msg" in valid_json
    assert "hostname" in valid_json
    assert "v" in valid_json


def test_bunyan_correct_values(
    log_record: logging.LogRecord, bunyan_formatter: logging.Formatter
) -> None:
    """Test that the bunyan formatter contains all relevant values."""
    formatted_log: str = bunyan_formatter.format(log_record)

    assert (re.search(
        r"\"time\": \"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z\"",
        formatted_log
    ) is not None)

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, object] = json.loads(formatted_log)

    # Ensure all required values are the correct type
    assert isinstance(valid_json["time"], str)
    assert isinstance(valid_json["name"], str)
    assert isinstance(valid_json["pid"], int)
    assert isinstance(valid_json["level"], int)
    assert isinstance(valid_json["msg"], str)
    assert isinstance(valid_json["hostname"], str)
    assert isinstance(valid_json["v"], int)

    # Ensure the correct values are present

    assert (re.search(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
        valid_json["time"]
    ) is not None)
    time_expected: str = USE_DATETIME.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    assert valid_json["time"] == time_expected
    assert valid_json["name"] == "root"
    assert valid_json["level"] == 10
    assert valid_json["msg"] == "A demo log message"
    assert valid_json["hostname"] == "SomePc"
    assert valid_json["v"] == 0


def test_bunyan_string_formatting(
    args_log_record: logging.LogRecord, bunyan_formatter: logging.Formatter
) -> None:
    """Test that the bunyan formatter formats message strings correctly."""
    formatted_log: str = bunyan_formatter.format(args_log_record)

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, object] = json.loads(formatted_log)

    assert valid_json["msg"] == "A message with formatting"


def test_bunyan_extras(
    extra_log_record: logging.LogRecord, bunyan_formatter: logging.Formatter
) -> None:
    """Test that the bunyan formatter adds extra values in."""
    formatted_log: str = bunyan_formatter.format(extra_log_record)

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, object] = json.loads(formatted_log)

    assert "str_extra" in valid_json
    assert valid_json["str_extra"] == "Extra 1"
    assert "int_extra" in valid_json
    assert valid_json["int_extra"] == 2
    assert "float_extra" in valid_json
    assert valid_json["float_extra"] == 1.5
