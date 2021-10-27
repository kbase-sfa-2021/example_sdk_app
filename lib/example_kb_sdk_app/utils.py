from base import Core


class ExampleAppClients:
    def __init__(self, callback_url, clients):
        self.KBaseReport = clients["KBaseReport"](callback_url)
        self.ReadsUtils = clients["ReadsUtils"](callback_url)


class ExampleReadsApp(Core):

    def __init__(self, ctx, config, clients_class=None):
        super().__init__(ctx, config, clients_class)
        self.ru = self.clients.ReadsUtils


    def do_analysis(self, params:dict):
        read_refs = params['reads_refs']
        return self.download_reads(read_refs)



    def download_reads(self, reads_refs, interleaved=False):
        """
        Download a list of reads objects
        param: reads_refs - A list of reads references/upas
        """

        dr_params = {'read_libraries': [reads_refs], 'interleaved': None}
        ret = self.ru.download_reads(dr_params)
        from pprint import pprint
        pprint(ret)
        return ret
        # read_file_list = list()
        # for file in ret['files']:
        #     obj_info = self.dfu.get_objects({'object_refs': [file]})['data'][0]['info']
        #     obj_name = obj_info[1]
        #     obj_ref_suffix = '_' + str(obj_info[6]) + '_' + str(obj_info[0]) + '_' + str(obj_info[4])
        #
        #     files = ret['files'][file]['files']
        #
        #     fwd_name = files['fwd'].split('/')[-1]
        #     fwd_name = fwd_name.replace('.gz', '')
        #     # using object_name + ref_suffix + suffix as file name
        #     fwd_name = obj_name + obj_ref_suffix + '.' + fwd_name.split('.', 1)[-1]
        #     shutil.move(files['fwd'], os.path.join(read_file_path, fwd_name))
        #     read_file_list.append(os.path.join(read_file_path, fwd_name))
        #
        #     if (files['rev'] is not None):
        #         rev_name = files['rev'].split('/')[-1]
        #         rev_name = rev_name.replace('.gz', '')
        #         rev_name = obj_name + obj_ref_suffix + '.' + rev_name.split('.', 1)[-1]
        #         shutil.move(files['rev'], os.path.join(read_file_path, rev_name))
        #         read_file_list.append(os.path.join(read_file_path, rev_name))(obj_info[0]) + '_' + str(obj_info[4])
        #         info[0]) + '_' + str(obj_info[4])
