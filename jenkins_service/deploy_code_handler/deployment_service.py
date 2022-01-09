"""
  File : deployment_service.py
  Description: This document will handle deployment api resources
  Author: TATA ELXSI
  List of Functions: post

"""

from flask_restful import Resource
from flask import request, Response
from jenkins_service import JenkinsService


class DeploymentService(Resource):
    """
    This will hold api resources for deployment
    """

    def __init__(self, config, logger):
        self.config = config
        self.deployment_info = None
        self.logger = logger.set_logger(__name__)
        self.jenkins_service = JenkinsService(self.config, logger)
        self.default_content_type = 'application/json'

    def post(self):
        """
        will handle the post method of deployment
        :return: response, json
        """
        Response.content_type = self.default_content_type
        self.deployment_info = request.json
        return self.jenkins_service.deploy_production(self.deployment_info)
