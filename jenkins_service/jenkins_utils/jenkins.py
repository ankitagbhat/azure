"""
  File : jenkins.py
  Description: This file contains functions related to jenkins job trigger
  Author: TATA ELXSI
  Version:
  List of Functions :write_orchestrator
                     write_vim
                     write_k8s_info
                     trigger_job
"""


class JenkinsJob:
    """
    This class will edit the claybot Common_config_data.yaml file and trigger the jenkins job
    """
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def write_orchestrator(self, orchestrator_details):
        """
        This function will edit the environment details
        :param orchestrator_details:
        :return:None
        """
        try:

            self.logger.info(orchestrator_details)

        except FileNotFoundError as write_orchestrator_error:
            error_msg = self.config['Response']['FILE_EXCEPTION'] + str(write_orchestrator_error)
            self.logger.error(error_msg)
            raise FileNotFoundError from write_orchestrator_error

        except Exception as write_orchestrator_error:
            error_msg = self.config['Response']['General_exception'] + str(write_orchestrator_error)
            self.logger.error(error_msg)
            raise Exception from write_orchestrator_error

    def write_vim(self, vim_details):
        """
        This function will edit the inputs of yaml file
        :param vim_details
        :return:None
        """
        try:

            self.logger.info(vim_details)

        except FileNotFoundError as write_vim_error:
            error_msg = self.config['Response']['FILE_EXCEPTION'] + str(write_vim_error)
            self.logger.error(error_msg)
            raise FileNotFoundError from write_vim_error

        except Exception as write_vim_error:
            error_msg = self.config['Response']['General_exception'] + str(write_vim_error)
            self.logger.error(error_msg)
            raise Exception from write_vim_error

    def write_k8s_info(self, payload):
        """
        This function will write the kubernetes repo to config file
        :param payload:
        :param config:
        :return: None
        """
        try:

            self.logger.info(payload)

        except FileNotFoundError as write_k8s_error:
            error_msg = self.config['Response']['FILE_EXCEPTION'] + str(write_k8s_error)
            self.logger.error(error_msg)
            raise FileNotFoundError from write_k8s_error

        except Exception as write_k8s_error:
            error_msg = self.config['Response']['General_exception'] + str(write_k8s_error)
            self.logger.error(error_msg)
            raise Exception from write_k8s_error

    def trigger_job(self, jenkins_job_name, params):
        """
        This will trigger the jenkins job
        :param config:
        :param jenkins_job_name:
        :param params:
        :return: result of job, string
        """
        try:

            self.logger.info(jenkins_job_name, params)

        except Exception as trigger_job_error:
            error_msg = self.config['Response']['General_exception'] + str(trigger_job_error)
            self.logger.error(error_msg)
            raise Exception from trigger_job_error
