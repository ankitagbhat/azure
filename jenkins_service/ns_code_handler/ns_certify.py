"""
File : ns_certify.py
Description: This file responsible for ns certification
Author: TATA ELXSI
List of Functions : ns_certify
"""
from jenkins_base_class.jenkins_base_class import JenkinsBaseClass


class NetworkServiceHandler(JenkinsBaseClass):
    """
    This class is for testing network services
    :returns json
    """

    def __init__(self, config, logger):
        super(NetworkServiceHandler, self).__init__(config, logger)
        self.job_name = self.config['JenkinsJob']['NS_JOB']
        self.service_name = self.config['Constant']['NS_TEST']

    def certify_ns(self, payload):
        """
        This will trigger the job for ns testing
        :param payload:
        :return: response, json
        """

        try:
            verify_payload = self.verify_payload.verify_ns_payload(ns_payload=payload)
            if verify_payload:

                params, vim_details, orchestrator_details = self.params_constructor.get_details_payload(
                    self.service_name, payload)

                # writing vim and orchestrator details
                self.write_config(vim_details=vim_details, orchestrator_details=orchestrator_details)

                # writing the k8repo details
                if payload['nfDetails'][0]['nfPackageType'] == 'KNF':
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
                                                     "Exception occurred in ns certify: {}".format(error))
