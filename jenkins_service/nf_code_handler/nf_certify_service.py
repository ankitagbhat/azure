"""
  File : nf_certify_service.py
  Description: This document will handle nf_certify api resources
  Author: TATA ELXSI
  List of Functions: post

"""

from flask_restful import Resource
from flask import request, Response
from jenkins_service import JenkinsService


class NfCertificationService(Resource):
    """
    This will hold api resources of NF certify
    """

    def __init__(self, config, logger):
        self.config = config
        self.nf_certify_info = None
        self.logger = logger.set_logger(__name__)
        self.jenkins_service = JenkinsService(self.config, logger)
        self.default_content_type = 'application/json'

    def post(self):
        """
        Will handle the post method of nf certify
        :return: response, json
        """
        Response.content_type = self.default_content_type
        self.nf_certify_info = request.json
        return self.jenkins_service.certify_nf(self.nf_certify_info)
