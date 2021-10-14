from installed_clients.KBaseReportClient import KBaseReport

class Clients:
    def __init__(self, callback_url):
        self.KBaseReport = KBaseReport(callback_url)

class Core:
    def __init__(self, ctx, config):
        self.callback_url = config.get("callback_url")
        self.ctx = ctx
        self.clients = Clients(self.callback_url)

    def do_analysis(self, params:dict):
        self.validate_do_analysis(params)
        report_info = self.clients.KBaseReport.create({
            'report': {
                'objects_created': [],
                'text_message': params['param_1']
            },
            'workspace_name': params['workspace_name']
        })
        return {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }

    def validate_do_analysis(self, params:dict):
        param_1 = params.get("param_1")
        if not isinstance(param_1, str):
            raise Exception("Please provide a string for param_1.")

        param_2 = params.get("param_2")
        if not isinstance(param_2, list):
            raise Exception("Please provide a list for param_2.")

        param_3 = params.get("param_3")
        if not isinstance(param_3, dict):
            raise Exception("Please provide a dict for param_3.")

        param_4 = params.get("param_4")
        if not (0 < param_4 < 100):
            raise Exception(
                "Please provide a between 0 and 100 for param_4"
            )
