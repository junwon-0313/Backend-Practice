#### 1. logging module 써보기
import logging

#loggin은 기본적으로 warning부터 출력되게 설정되어 있음.
logger = logging.getLogger("example")  # root logger
logger.info("hello world")  # 아무런 로그도 출력되지 않습니다.

#### 1.1 logging module config 추가하기
import logging.config

logger_config = {
    "version": 1,  # required
    "disable_existing_loggers": True,  # 다른 Logger를 overriding 합니다
    "formatters": {
        "simple": {"format": "%(asctime)s | %(levelname)s - %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "loggers": {"example": {"level": "INFO", "handlers": ["console"]}},
}

logging.config.dictConfig(logger_config)
logger_with_config = logging.getLogger("example")
logger_with_config.info("이제는 보이죠?")

#### 1.2 dynamic logging config
dynamic_logger = logging.getLogger()
log_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s | %(levelname)s - %(message)s")
log_handler.setFormatter(formatter)
dynamic_logger.addHandler(log_handler)

dynamic_logger.info("hello world")