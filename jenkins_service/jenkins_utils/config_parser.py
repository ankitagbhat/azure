"""
  File : config_parser.py
  Description: This document will validate the config
  Author: TATA ELXSI
  List of Functions: verify_config
"""

import configparser
from jenkins_utils.logger_func import Logger


class ConfigParse:
    """
    Responsible for validating correct config
    """

    def __init__(self):
        self.parse_config = configparser.ConfigParser()
        self.logger = Logger.set_logger(__name__)

    def read_config(self):
        """
        This will read the config
        :return: config, config object
        """
        try:
            self.parse_config.read("config.cfg")
            return self.parse_config

        except KeyError as error:
            self.logger.info("Error in reading the config" + str(error))
            return None

        except Exception as error:
            self.logger.info("Exception occurred while parsing the config file" + str(error))
            return None
