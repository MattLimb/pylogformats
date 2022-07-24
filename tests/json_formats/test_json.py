"""Test cases for the Bunyan Formatter."""

import datetime
import json
import logging
import re
from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Union

import pytest

from pylogformats.json import JsonFormat


USE_DATETIME = datetime.datetime.utcnow()


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
    record.__dict__["relativeCreated"] = USE_DATETIME.timestamp()
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
    record.__dict__["relativeCreated"] = USE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"

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
    record.__dict__["relativeCreated"] = USE_DATETIME.timestamp()
    record.__dict__["hostname"] = "SomePc"

    # Extras
    record.__dict__["str_extra"] = "Extra 1"
    record.__dict__["int_extra"] = 2
    record.__dict__["float_extra"] = 1.5

    return record


@pytest.fixture
def json_formatter() -> logging.Formatter:
    """Fixture for creating a formatter class."""
    return JsonFormat()


def test_json_correct_keys(
    log_record: logging.LogRecord, json_formatter: logging.Formatter
) -> None:
    """Test that the JSON formatter contains all relevant keys."""
    formatted_log: str = json_formatter.format(log_record)

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, Any] = json.loads(formatted_log)

    # Ensure all required keys are present
    assert "logger" in valid_json
    assert "timestamp" in valid_json
    assert "message" in valid_json
    assert "level" in valid_json
    assert "levelno" in valid_json
    assert "function" in valid_json

    assert "process" in valid_json
    process: Dict[str, Any] = valid_json["process"]
    assert "number" in process
    assert "name" in process

    assert "thread" in valid_json
    thread: Dict[str, Any] = valid_json["thread"]
    assert "number" in thread
    assert "name" in thread

    assert "v" in valid_json


def test_json_correct_values(
    log_record: logging.LogRecord, json_formatter: logging.Formatter
) -> None:
    """Test that the JSON formatter contains all relevant values."""
    formatted_log: str = json_formatter.format(log_record)

    assert (
        re.search(
            r"\"timestamp\": \"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}\"",
            formatted_log,
        )
        is not None
    )

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, Any] = json.loads(formatted_log)

    # Ensure all required values are the correct type
    assert isinstance(valid_json["logger"], str)
    assert isinstance(valid_json["timestamp"], str)
    assert isinstance(valid_json["message"], str)
    assert isinstance(valid_json["level"], str)
    assert isinstance(valid_json["levelno"], int)
    assert isinstance(valid_json["function"], str)

    assert isinstance(valid_json["process"], dict)
    process: Dict[str, Any] = valid_json["process"]
    assert isinstance(process["number"], int)
    assert isinstance(process["name"], str)

    assert isinstance(valid_json["thread"], dict)
    thread: Dict[str, Any] = valid_json["thread"]
    assert isinstance(thread["number"], int)
    assert isinstance(thread["name"], str)

    assert isinstance(valid_json["v"], int)

    # Ensure the correct values are present

    assert (
        re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}", valid_json["timestamp"])
        is not None
    )

    assert valid_json["logger"] == "root"
    assert valid_json["timestamp"] == USE_DATETIME.isoformat()
    assert valid_json["message"] == "A demo log message"
    assert valid_json["level"] == "DEBUG"
    assert valid_json["levelno"] == 10
    assert valid_json["function"] == "test_json"

    assert process["name"] == "MainProcess"
    assert thread["name"] == "MainThread"

    assert valid_json["v"] == 1


def test_json_string_formatting(
    args_log_record: logging.LogRecord, json_formatter: logging.Formatter
) -> None:
    """Test that the JSON formatter formats message strings correctly."""
    formatted_log: str = json_formatter.format(args_log_record)

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, Any] = json.loads(formatted_log)

    assert valid_json["message"] == "A message with formatting"


def test_json_extras(
    extra_log_record: logging.LogRecord, json_formatter: logging.Formatter
) -> None:
    """Test that the JSON formatter adds extra values in."""
    formatted_log: str = json_formatter.format(extra_log_record)

    # Ensure that the string is a valid JSON string
    valid_json: Dict[str, object] = json.loads(formatted_log)

    assert "str_extra" in valid_json
    assert valid_json["str_extra"] == "Extra 1"
    assert "int_extra" in valid_json
    assert valid_json["int_extra"] == 2
    assert "float_extra" in valid_json
    assert valid_json["float_extra"] == 1.5
