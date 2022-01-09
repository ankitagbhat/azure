"""
#  File : jenkins_app.py
#  Description: This file contains main file which run flask app
#  Author: TATA ELXSI
#  List of classes :  JenkinsResult
"""
import sys
from flask import Flask, request, Response
from flask_restful import Resource, Api
from jenkins_utils.config_parser import ConfigParse
from nf_code_handler.nf_certify_service import NfCertificationService
from ns_code_handler.ns_certify_service import NsCertificationService
from candidate_code_handler.candidate_service import CandidateService
from deploy_code_handler.deployment_service import DeploymentService
from jenkins_service import JenkinsService
from jenkins_utils.logger_func import Logger


class JenkinsResult(Resource):
    """
    This will hold api resources for jenkins result
    """

    def __init__(self):
        self.jenkins_result_info = None
        self.jenkins_service = JenkinsService(config)

    def post(self):
        """
        will handle the post method of jenkins result
        :return: None
        """
        Response.content_type = 'application/json'
        self.jenkins_result_info = request.json
        return self.jenkins_service.get_job_result(self.jenkins_result_info)


def initiator():
    """
    Initiator which initiates logger
    :return: logger
    """
    logger = Logger()

    return logger


def resource_allocator(api, config, logger_val):
    """
    Adding restful resources
    :param logger_val:
    :param config:
    :param api:
    :return: None
    """
    api.add_resource(NfCertificationService, '/teatom/v1/nf_certify',
                     resource_class_kwargs={'config': config, 'logger': logger_val})
    api.add_resource(NsCertificationService, '/teatom/v1/ns_certify',
                     resource_class_kwargs={'config': config, 'logger': logger_val})
    api.add_resource(CandidateService, '/teatom/v1/candidate',
                     resource_class_kwargs={'config': config, 'logger': logger_val})
    api.add_resource(DeploymentService, '/teatom/v1/deploy',
                     resource_class_kwargs={'config': config, 'logger': logger_val})
    api.add_resource(JenkinsResult, '/teatom/v1/result')


if __name__ == "__main__":
    jenkins_app = Flask(__name__)
    config = ConfigParse().read_config()
    if config:
        api = Api(jenkins_app)
        logger_value = initiator()
        resource_allocator(api, config, logger_value)
        jenkins_app.run(host=config['Default']['HOST'], port=int(config['Default']['PORT']),
                        debug=config['Default']['DEBUG'])
    else:
        sys.exit('Error while parsing the config while')

    sys.exit('successfully executed the operation')
