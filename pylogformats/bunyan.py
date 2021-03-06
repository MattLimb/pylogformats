import logging
import platform
import json
from datetime import datetime

BASELINE = vars(logging.LogRecord(*[None for _ in range(9)]))

class BunyanFormat(logging.Formatter):
    """ A Simple Bunyan JSON Format """
    def format(self, record):
        fr = dict(
            time=datetime.fromtimestamp(getattr(record, "created")).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
            name=getattr(record, "name"),
            pid=getattr(record, "process"),
            level=getattr(record, "levelno"),
            msg=getattr(record, "msg"),
            hostname=platform.node(),
            v=0
        )

        extras = dict()

        for key, value in vars(record).items():
            if key not in BASELINE:
                extras[key] = value

        if len(extras) != 0:
            fr.update(extras)
        
        return json.dumps(fr)
