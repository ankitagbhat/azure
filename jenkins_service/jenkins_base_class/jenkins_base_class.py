"""
File : jenkins_base_class.py
Description: parent class for handling nf, ns, candidate, deploy code handlers
Author: TATA ELXSI
List of Functions : __init__
                    get_details
                    write_config
                    write_k8s_config
                    trigger_jenkins_job
"""

from jenkins_utils.params_constructor import ParamsConstructor
from jenkins_utils.verify_payload import VerifyPayload
from jenkins_utils.jenkins import JenkinsJob
from jenkins_utils.response_builder import ResponseBuilder


class JenkinsBaseClass:
    """
    This class is for handling nf, ns, candidate and deployment
    :returns json
    """

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger.set_logger(__name__)
        self.jenkins = JenkinsJob(self.config, self.logger)
        self.response_builder = ResponseBuilder(self.config)
        self.params_constructor = ParamsConstructor(self.config, self.logger)
        self.verify_payload = VerifyPayload(self.config, self.logger)
        self.payload_error = self.config['Response']['PAYLOAD_ERROR']
        self.file_exception = self.config['Response']['FILE_EXCEPTION']
        self.job_error = self.config['Response']['JOB_ERROR']

    def get_details(self, service_name, payload):
        """
        This will construct params as per the service_name
        :param service_name:
        :param payload:
        :return:
        """
        try:
            params, vim_details, orchestrator_details = self.params_constructor.get_details_payload(service_name,
                                                                                                    payload)
            return params, vim_details, orchestrator_details

        except KeyError as get_details_error:
            error_msg = self.payload_error
            raise KeyError(get_details_error) from get_details_error

    def write_config(self, vim_details, orchestrator_details):
        """
        This will write the configuration
        :param orchestrator_details:
        :param vim_details:
        :return: None
        """
        try:
            self.jenkins.write_vim(vim_details=vim_details)
            self.jenkins.write_orchestrator(orchestrator_details=orchestrator_details)

        except FileNotFoundError as write_config_error:
            error_msg = self.file_exception
            raise KeyError(write_config_error) from write_config_error

    def write_k8s_config(self, payload):
        """
        This will write the k8s configuration
        :param payload:
        :return:
        """
        try:
            self.jenkins.write_k8s_info(payload)

        except FileNotFoundError as write_k8s_config_error:
            error_msg = self.file_exception + str(write_k8s_config_error)
            raise KeyError(write_k8s_config_error) from write_k8s_config_error

    def trigger_jenkins_job(self, job_name, params):
        """
        This will trigger the jenkins job with given job name
        :param params:
        :param job_name:
        :return: result: string
        """
        try:
            self.jenkins.trigger_job(jenkins_job_name=job_name, params=params)
        except ConnectionRefusedError as trigger_jenkins_job_error:
            raise Exception(trigger_jenkins_job_error) from trigger_jenkins_job_error
