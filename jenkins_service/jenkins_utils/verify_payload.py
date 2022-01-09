"""
  File : jenkins.py
  Description: This file create params required by jenkins job.
  Author: TATA ELXSI
  Version:
  List of Functions : key_verification
                     verify_nf_payload
                     verify_ns_payload
                     verify_candidate_payload
                     verify_production_deploy_payload
"""


class VerifyPayload:

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    @classmethod
    def key_verification(cls, request_payload, payload_keys):
        """
        This will verify that all the keys are present
        :param payload_keys:
        :param request_payload:
        :return: status, bool
        """
        return True

    @classmethod
    def verify_nf_payload(cls, nf_payload):
        """
        This will check whether the payload given has all the fields required to trigger nf job
        :param nf_payload:
        :return:status, bool
        """
        return True

    @classmethod
    def verify_ns_payload(cls, ns_payload):
        """
        This will check whether the payload given has all the fields required to trigger ns job
        :param ns_payload:
        :return: status, bool
        """
        return True

    @classmethod
    def verify_candidate_payload(cls, candidate_payload):
        """
        This will check whether the payload given has all the fields required to trigger candidate job
        :param candidate_payload:
        :return: status, bool
        """

        return True

    @classmethod
    def verify_production_deploy_payload(cls, production_deploy_payload):
        """
        This will check whether payload given has all the fields required to trigger production deployment
        :param production_deploy_payload:
        :return: status, bool
        """
        return True
