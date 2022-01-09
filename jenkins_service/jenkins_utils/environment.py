"""
  File : environment.py
  Description: This module modifies vim and orchestrator details
  Author: TATA ELXSI
  List of Functions: __init__
                     fetch_vim_details
                     fetch_orchestrator_details
"""


class Environment:
    """
    Environment class edits the configuration as per user inputs
    """

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def fetch_vim_details(self, payload):
        """
        This will fetch the vim details from payload
        :param payload:
        :return: vim_details, dict
        """
        try:
            self.logger.info(payload)
            vim_details = {}
            return vim_details

        except KeyError as fetch_vim_error:
            error_msg = self.config['logging']['key_error'] + str(fetch_vim_error)
            self.logger.error(error_msg)
            raise KeyError from fetch_vim_error

    def fetch_orchestrator_details(self, payload):
        """
        This will fetch the orchestrator details
        :param payload:
        :return: orchestrator_details, dict
        """
        try:
            self.logger.info(payload)
            orchestrator_details = {}
            return orchestrator_details

        except KeyError as fetch_orchestrator_error:
            error_msg = self.config['logging']['key_error'] + str(fetch_orchestrator_error)
            self.logger.error(error_msg)
            raise KeyError from fetch_orchestrator_error
