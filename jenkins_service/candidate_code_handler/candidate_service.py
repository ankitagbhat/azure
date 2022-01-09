"""
  File : candidate_service.py
  Description: This document will handle candidate api resources
  Author: TATA ELXSI
  List of Functions: post

"""
from flask_restful import Resource
from flask import request, Response
from jenkins_service import JenkinsService


class CandidateService(Resource):
    """
    This will hold api resources for candidate
    """

    def __init__(self, config, logger):
        self.config = config
        self.candidate_info = None
        self.logger = logger.set_logger(__name__)
        self.jenkins_service = JenkinsService(self.config, logger)
        self.default_content_type = 'application/json'

    def post(self):
        """
        will handle the post method of candidate
        :return: response, json
        """
        Response.content_type = self.default_content_type
        self.candidate_info = request.json
        return self.jenkins_service.upload_artifacts(self.candidate_info)
