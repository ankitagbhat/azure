"""
File : nf_certify.py
Description: This file responsible for nf certification
Author: TATA ELXSI
List of Functions : nf_certify
"""
from jenkins_base_class.jenkins_base_class import JenkinsBaseClass


class NetworkFunctionHandler(JenkinsBaseClass):
    """
    This class is for testing network functions
    :returns json
    """

    def __init__(self, config, logger):
        super(NetworkFunctionHandler, self).__init__(config, logger)
        self.job_name = self.config['JenkinsJob']['NF_JOB']
        self.service_name = self.config['Constant']['NF_TEST']

    def certify_nf(self, payload):
        """
        This will trigger the jenkins job of nf_testing
        :param payload: json
        :return: response, json
        """
        try:
            verify_payload = self.verify_payload.verify_nf_payload(nf_payload=payload)
            if verify_payload:

                params, vim_details, orchestrator_details = self.get_details(self.service_name, payload)

                # writing vim and orchestrator details
                self.write_config(vim_details=vim_details, orchestrator_details=orchestrator_details)

                # writing the k8repo details
                if payload['nfPackageType'] == 'KNF':
                    self.write_k8s_config(payload=payload)

                # Triggering the nf_testing job with necessary parameters
                result = self.jenkins.trigger_job(self.job_name, params)

        except KeyError as key_error:
            error_msg = self.payload_error
            return self.response_builder.bad_request(error_msg,
                                                     "Invalid key in payload {}".format(key_error))

        except FileNotFoundError as not_found:
            error_msg = self.file_exception
            return self.response_builder.file_exception(error_msg,
                                                        "File not found while writing config {}".format(not_found))

        except Exception as error:
            error_msg = self.job_error
            return self.response_builder.bad_request(error_msg,
                                                     "Exception occurred in nf certify: {}".format(error))
