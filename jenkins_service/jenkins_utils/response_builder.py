"""
  File : response_builder.py
  Description: This file will handle responses required by microservice.
  Author: TATA ELXSI
  Version:
  List of Functions :success_resp
                     bad_request
                     failure_resp
                     file_exception
                     jenkins_exception
                     internal_server_error
                     unauthorized_resp
"""

import json
from http import HTTPStatus
from flask import Response


class ResponseBuilder:
    """
    Class which will handle all the response codes
    """

    def __init__(self, config):
        self.config = config

    def success_resp(self, success_msg):
        """
        Success response
        :param success_msg:
        :return: response, Response
        """
        success = {
            'statusMessage': success_msg
        }
        return Response(json.dumps(success), HTTPStatus.OK, mimetype=self.config['Response']['Default_response'])

    def bad_request(self, error_msg):
        """
        bad request response
        :param error_msg:
        :return: response, Response
        """
        error = {
            'errorMessage': error_msg
        }
        return Response(json.dumps(error), HTTPStatus.BAD_REQUEST, mimetype=self.config['Response']['Default_response'])

    def failure_resp(self, failure_msg):
        """
        failure request response
        :param failure_msg:
        :return: response, Response
        """
        failure = {
            'statusMessage': failure_msg
        }
        return Response(json.dumps(failure), HTTPStatus.BAD_REQUEST,
                        mimetype=self.config['Response']['Default_response'])

    def file_exception(self, file_exception_msg):
        """
        file exception response
        :param file_exception_msg:
        :return: response, Response
        """
        failure = {
            'statusMessage': file_exception_msg
        }
        return Response(json.dumps(failure), HTTPStatus.NOT_FOUND, mimetype=self.config['Response']['Default_response'])

    def jenkins_exception(self, jenkins_exception_msg):
        """
        jenkins exception request response
        :param jenkins_exception_msg:
        :return: response, Response
        """
        failure = {
            'statusMessage': jenkins_exception_msg
        }
        return Response(json.dumps(failure), HTTPStatus.INTERNAL_SERVER_ERROR,
                        mimetype=self.config['Response']['Default_response'])

    def internal_server_error(self, error_msg):
        """
        internal server error request response
        :param error_msg:
        :return: response, Response
        """
        error = {
            'errorMessage': error_msg
        }
        return Response(json.dumps(error), HTTPStatus.INTERNAL_SERVER_ERROR,
                        mimetype=self.config['Response']['Default_response'])

    def unauthorized_resp(self, error_msg):
        """
        unauthorized request response
        :param error_msg:
        :return: response, Response
        """
        error = {
            'errorMessage': error_msg
        }
        return Response(json.dumps(error), HTTPStatus.UNAUTHORIZED,
                        mimetype=self.config['Response']['Default_response'])
