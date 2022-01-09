"""
File : candidate.py
Description: This file responsible for artifacts upload
Author: TATA ELXSI
List of Functions : __init__
                    upload_packages
"""

from jenkins_base_class.jenkins_base_class import JenkinsBaseClass


class CandidateHandler(JenkinsBaseClass):
    """
    This class is for uploading artifacts
    :returns json

    """
    def __init__(self, config, logger):
        super(CandidateHandler, self).__init__(config, logger)
        self.job_name = self.config['JenkinsJob']['CANDIDATE_JOB']

    def upload_packages(self, payload):
        """
        This will trigger the job for uploading of artifacts
        :param payload:
        :return:
        """
        try:
            verify_payload = self.verify_payload.verify_candidate_payload(payload)
            if verify_payload:
                params = self.params_constructor.certify_candidate_param(payload)

                # Triggering the candidate job with necessary parameters
                result = self.jenkins.trigger_job(self.job_name, params)

        except Exception as error:
            error_msg = self.job_error
            return self.response_builder.bad_request(error_msg, "Exception occurred in candidate {}".format(error))
