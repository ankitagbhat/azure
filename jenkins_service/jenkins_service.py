"""
  File : jenkins_service.py
  Description: This document will handle api resources
  Author: TATA ELXSI
  List of Functions: certify_nf
                     certify_ns
                     upload_artifacts
                     deploy_production
                     get_job_result
"""
from nf_code_handler.nf_certify import NetworkFunctionHandler
from ns_code_handler.ns_certify import NetworkServiceHandler
from candidate_code_handler.candidate import CandidateHandler
from deploy_code_handler.deployment import DeployHandler
from jenkins_base_class.jenkins_base_class import JenkinsBaseClass

class JenkinsService:
    """
    Will hold apis of jenkins microservices
    """

    def __init__(self, config, logger):
        self.config = config
        self.class_object = None
        self.logger = logger.set_logger(__name__)
        self.jenkins_base_class = JenkinsBaseClass(self.config, logger)
        self.nf_certification = NetworkFunctionHandler(self.config, logger)
        self.ns_certification = NetworkServiceHandler(self.config, logger)
        self.candidate = CandidateHandler(self.config, logger)
        self.deployment_ns = DeployHandler(self.config, logger)

    def certify_nf(self, nf_config):
        """
        certifying the nf packages
        :param nf_config:
        :return:response, json
        """

        return self.nf_certification.certify_nf(nf_config)

    def certify_ns(self, ns_config):
        """
        ns certification of packages
        :param ns_config:
        :return:response,json
        """

        return self.ns_certification.certify_ns(payload=ns_config)

    def upload_artifacts(self, upload_config):
        """
        upload of ns packages
        :param upload_config:
        :return:response,json
        """

        return self.candidate.upload_packages(payload=upload_config)

    def deploy_production(self, deploy_config):
        """
        Deployment of packages to production
        :param deploy_config:
        :return:response,json
        """
        return self.deployment_ns.deploy_production(payload=deploy_config)

    def get_job_result(self, result_config):
        """
        Result of jenkins job
        :return: None
        """
        return None
