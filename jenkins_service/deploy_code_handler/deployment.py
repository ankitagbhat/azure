"""
File : deployment.py
Description: Handles artifacts download from artifactory and deploy the same  to production
Author: TATA ELXSI
List of Functions : __init__
                    production_deploy
"""
from jenkins_base_class.jenkins_base_class import JenkinsBaseClass


class DeployHandler(JenkinsBaseClass):
    """
    This will handle deployment
    """

    def __init__(self, config, logger):
        super(DeployHandler, self).__init__(config, logger)
        self.artifacts_download_job = self.config['JenkinsJob']['ARTIFACT_DOWNLOAD_JOB']
        self.job_name = self.config['JenkinsJob']['DEPLOY_JOB']
        self.service_name = self.config['Constant']['DEPLOY']

    def artifacts_download(self, payload):
        """
        This will download artifacts from Artifactory
        :param payload:
        :return:
        """
        try:
            params = self.params_constructor.download_artifacts_param(payload)
            return params

        except Exception as artifacts_download_error:
            raise Exception from artifacts_download_error

    def deploy_production(self, payload):
        """
        This will download artifacts from Artifactory and deploy the same artifacts to production
        :param payload:
        :return:
        """
        try:
            verify_payload = self.verify_payload.verify_production_deploy_payload(payload)

            if verify_payload:

                # Getting the params in dictionary format to trigger nf testing job
                params = self.artifacts_download(payload)

                # Triggering the candidate job with necessary parameters
                result = self.jenkins.trigger_job(self.artifacts_download_job, params)

                params, vim_details, orchestrator_details = self.params_constructor.get_details_payload(
                    self.service_name, payload)

                # writing vim and orchestrator details
                self.write_config(vim_details=vim_details, orchestrator_details=orchestrator_details)

                # writing the k8repo details
                if payload['nfDetails'][0]['nfPackageType'] == 'KNF':
                    self.write_k8s_config(payload=payload)

                # Triggering the deployment job with necessary parameters
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
                                                     "Exception occurred in deployment {}".format(error))
