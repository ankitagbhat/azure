"""
  File : logger_func.py
  Description: This is logging module
  Author: TATA ELXSI
  List of Functions: set_logger
"""
import logging
import os
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = '%(asctime)s : %(name)s :: %(message)s'
LOGGER_PATH = '/apps/logs/jenkins'
JENKINS_LOG_FILENAME = '/apps/logs/jenkins/jenkins.log'


class Logger:
    """
    This class will handle logging
    """
    @staticmethod
    def set_logger(name):
        """
        This function will do logging of modules
        :param name:
        :return: logger, logger object
        """
        if not os.path.isdir(LOGGER_PATH):
            os.makedirs(LOGGER_PATH)
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler = TimedRotatingFileHandler(JENKINS_LOG_FILENAME, when='D', interval=1,
                                                backupCount=2, encoding=None, delay=False, utc=False, atTime=None)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        try:
            return logger

        except Exception as logger_error:
            raise Exception from logger_error
