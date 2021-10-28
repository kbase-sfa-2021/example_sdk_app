import logging
import os

from shutil import copyfile

from Bio import SeqIO

from base import Core


class ExampleReadsApp(Core):

    def __init__(self, ctx, config, clients_class=None):
        super().__init__(ctx, config, clients_class)
        self.ru = self.clients.ReadsUtils


    def do_analysis(self, params:dict):
        read_refs = params['reads_refs']
        ret = self.download_reads(read_refs)
        for file_ref, file_info in ret['files'].items():
            file_path = file_info['files']['fwd']
            basename = os.path.basename(file_path)
            with open(file_path) as reads:
                record_iter = SeqIO.parse(reads, "fastq")
                limit = 10
                head = []
                for ix, record in enumerate(record_iter):
                    if ix >= limit:
                        break
                    head.append(record)
                filename = f"{basename}.head.fastq"
                out_path = os.path.join(self.shared_folder, filename)
                with open(out_path, "w") as out_reads:
                    SeqIO.write(head, out_reads, "fastq")
        return dict()


    def download_reads(self, reads_refs, interleaved=False):
        """
        Download a list of reads objects
        param: reads_refs - A list of reads references/upas
        """

        dr_params = {'read_libraries': [reads_refs], 'interleaved': None}
        return self.ru.download_reads(dr_params)
