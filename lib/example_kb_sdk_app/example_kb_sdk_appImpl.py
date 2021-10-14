# -*- coding: utf-8 -*-
# BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from lib.example_kb_sdk_app.core import Core


# END_HEADER


class example_kb_sdk_app:
    '''
    Module Name:
    example_kb_sdk_app

    Module Description:
    A KBase module: example_kb_sdk_app
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    # BEGIN_CLASS_HEADER
    # END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        # BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        # END_CONSTRUCTOR
        pass

    def run_example_kb_sdk_app(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        # BEGIN run_example_kb_sdk_app

        param_1 = "str"
        param_2 = "list"
        param_3 = "dict"
        param_4 = "int"

        def validate(p1, p2, p3):
            if not isinstance(str, param_1):
                raise Exception("Wrong")

            if not (4 < param_4 < 100):
                raise Exception("Please provide range of params between 4 and 100")



        core = Core(ctx)
        output = core.do_analysis(params)

        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': {'objects_created': [],
                                                'text_message': params['parameter_1']},
                                     'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        # END run_example_kb_sdk_app

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_example_kb_sdk_app return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def status(self, ctx):
        # BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        # END_STATUS
        return [returnVal]
