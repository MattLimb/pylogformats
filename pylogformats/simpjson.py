import logging
import json
from datetime import datetime

BASELINE = vars(logging.LogRecord(*[None for _ in range(9)]))

class JSONFormat(logging.Formatter):
    """ A Simple JSON Logging Format. """

    def format(self, record):
        """Format the log based off the logRecord.

        Params:
        record: The LogRecord instance created by the log event.
        """
        
        formatted_message = getattr(record, "msg") % getattr(record, "args", tuple())

        fr = dict(
            logger=getattr(record, "name"),
            timestamp=datetime.fromtimestamp(getattr(record, "created")).isoformat(),
            message=formatted_message,
            level=getattr(record, "levelname"),
            levelno=getattr(record, "levelno"),
            function=getattr(record, "funcName"),
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
