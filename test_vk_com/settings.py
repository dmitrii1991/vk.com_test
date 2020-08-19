from datetime import datetime
from os.path import join, abspath, dirname
import logging.config

import structlog


ROOT_PATH = abspath(dirname(__file__))

LOGS_DIR = join(ROOT_PATH, "logs")

LINK_VK = "https://vk.com/"
TIME_WAIT = 10

timestamper = structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S")

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level_number,
        timestamper,
        structlog.processors.JSONRenderer(),
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory()
)


logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "plain": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.dev.ConsoleRenderer(colors=False),
            },
            "colored": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.dev.ConsoleRenderer(colors=True),
            },
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "colored",
                "stream": "ext://sys.stderr",
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": join(LOGS_DIR, 'test_vk_{:%d-%m-%Y}.log'.format(datetime.now())),
                "formatter": "plain",
                "mode": "a",
                "encoding": "utf-8"
            },
        },
        "loggers": {
            "": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": True,
            },
        }
})


logger_vk = structlog.get_logger('vk')
