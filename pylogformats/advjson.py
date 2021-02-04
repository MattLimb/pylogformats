import logging
import json
import platform
from datetime import datetime, timedelta

BASELINE = vars(logging.LogRecord(*[None for _ in range(9)]))

class AdvJSONFormat(logging.Formatter):
    """ JSON Formatter with all the bells and whistles. """

    def format(self, record):
        """Format the log based off the logRecord.

        Params:
        record: The LogRecord instance created by the log event.
        """
        fr = dict(
            logger=getattr(record, "name"),
            timestamp=datetime.fromtimestamp(getattr(record, "created")).isoformat(),
            rtimestamp=datetime.fromtimestamp(
                getattr(record, "created") - getattr(record, "relativeCreated")
            ).isoformat(),
            message=getattr(record, "msg"),
            level=getattr(record, "levelname"),
            levelno=getattr(record, "levelno"),
            location=dict(
                pathname=getattr(record, "pathname"),
                module=getattr(record, "module"),
                filename=getattr(record, "filename"),
                function=getattr(record, "funcName"),
                line=getattr(record, "lineno"),
            ),
            process=dict(
                number=getattr(record, "process"), 
                name=getattr(record, "processName")
            ),
            thread=dict(
                number=getattr(record, "thread"), 
                name=getattr(record, "threadName")
            ),
            v=1
        )

        extras = dict()

        for key, value in vars(record).items():
            if key not in BASELINE:
                extras[key] = value

        if len(extras) != 0:
            fr["extra"] = extras

        return json.dumps(fr)
