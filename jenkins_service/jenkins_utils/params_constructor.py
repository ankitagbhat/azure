"""
  File : jenkins.py
  Description: This file create params required by jenkins job.
  Author: TATA ELXSI
  Version:
  List of Functions :get_details_payload
                     certify_nf_param
                     certify_ns_param
                     certify_candidate_param
                     download_artifacts_param
                     deploy_production
"""

from jenkins_utils.environment import Environment


class ParamsConstructor:
    """
    construct parameters required for jenkins jobs
    """
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.environment = Environment(config, logger)

    def get_details_payload(self, module_name, payload):
        """
        This will extract details from given request
        :param module_name:
        :param payload:
        :return: params

        """
        try:
            params = {}
            # Getting the params in dictionary  to trigger nf testing job
            if module_name == self.config['Constant']['NF_TEST']:
                pass
            elif module_name == self.config['Constant']['NS_TEST']:
                pass
            elif module_name == self.config['Constant']['CANDIDATE']:
                pass
            elif module_name == self.config['Constant']['DEPLOY']:
                pass

            # Fetching the VIM details (openstack or AWS)
            vim_details = self.environment.fetch_vim_details(payload)

            # Fetching the orchestrator details from payload
            orchestrator_details = self.environment.fetch_orchestrator_details(payload)

            return params, vim_details, orchestrator_details

        except Exception as get_details_payload_error:
            error_msg = self.config['Response']['General_exception'] + str(get_details_payload_error)
            raise Exception from get_details_payload_error

    def certify_nf_param(self, payload):
        """
        Create the params required for nf testing job
        :param payload:
        :return: certify_nf_params, dict
        """
        try:

            return {}

        except KeyError as certify_nf_param_error:
            error_msg = self.config['logging']['key_error'] + str(certify_nf_param_error)
            raise KeyError from certify_nf_param_error

    def certify_ns_param(self, payload):
        """
        Create the params required for ns testing job
        :param payload:
        :return: certify_ns_params, dict
        """
        try:

            return {}

        except KeyError as certify_ns_param_error:
            error_msg = self.config['logging']['key_error'] + str(certify_ns_param_error)
            raise KeyError from certify_ns_param_error

    def certify_candidate_param(self, payload):
        """
        Create the params required for packages upload job
        :param payload:
        :return: candidate_params, dict
        """
        try:

            return {}

        except KeyError as certify_candidate_param_error:
            error_msg = self.config['logging']['key_error'] + str(certify_candidate_param_error)
            raise KeyError from certify_candidate_param_error

    def download_artifacts_param(self, payload):
        """
        This will return parameters to download artifacts from the JFROG Artifactory
        :param payload:
        :return: download_artifacts_params, dict
        """
        try:

            return {}

        except KeyError as download_artifacts_param_error:
            error_msg = self.config['logging']['key_error'] + str(download_artifacts_param_error)
            raise KeyError from download_artifacts_param_error

    def deploy_production(self, payload):
        """
        This will created params required for production_deployment
        :param payload:
        :return: deploy_params, dict
        """
        try:

            return {}

        except KeyError as deploy_production_error:
            error_msg = self.config['logging']['key_error'] + str(deploy_production_error)
            raise KeyError from deploy_production_error
