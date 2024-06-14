import logging
import logging.handlers
import time

class LoggerSetup():

    def __init__(self):
        self.logger = logging.getLogger('')
        self.setup_logging()

    def setup_logging(self):
        LOG_FORMAT = '{"time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": "%(message)s"}'
        logging.basicConfig(level=logging.INFO)

        formatter = logging.Formatter(LOG_FORMAT)

        console=logging.StreamHandler()
        console.setFormatter(formatter)

        log_file = "logs/app.log"
        file = logging.handlers.TimedRotatingFileHandler(log_file, when='M', interval=5, backupCount=3)
        file.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.addHandler(file)
