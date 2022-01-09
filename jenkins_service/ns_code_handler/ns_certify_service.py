"""
  File : ns_certify_service.py
  Description: This document will handle ns_certify api resources
  Author: TATA ELXSI
  List of Functions: post

"""
from flask_restful import Resource
from flask import request, Response
from jenkins_service import JenkinsService


class NsCertificationService(Resource):
    """
    This will hold api resources for ns certification
    """

    def __init__(self, config, logger):
        self.config = config
        self.ns_certify_info = None
        self.logger = logger.set_logger(__name__)
        self.jenkins_service = JenkinsService(self.config, logger)
        self.default_content_type = 'application/json'

    def post(self):
        """
        will handle the post method of ns certify
        :return: response, json
        """
        Response.content_type = self.default_content_type
        self.ns_certify_info = request.json
        return self.jenkins_service.certify_ns(self.ns_certify_info)
