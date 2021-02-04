LOG_CONFIG = {
  'formatters': {
    'AdvJSONFormat': {
      '()' : 'pylogformats.BunyanFormat'
    }
  },
  'handlers': {
    'debug': {
      'class': 'logging.StreamHandler',
      'formatter': 'AdvJSONFormat',
      'stream': 'ext://sys.stdout'
    },
  },

  'root': {
    'level': 'DEBUG',
    'handlers': ['debug']
  },
  'version': 1
}

import logging.config

logging.config.dictConfig(LOG_CONFIG)

logging.error("TEST ERROR")