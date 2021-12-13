# import logging
# import subprocess
#
# from pprint import pprint
# import pytest
# from unittest.mock import create_autospec, call
# from example_kb_sdk_app.utils import ExampleReadsApp
# from collections import namedtuple
#
# def kb_logger(process):
#     """
#     Prints stdout and stderr
#     Returns decoded stdout
#     """
#     stdout, stderr = process.communicate()
#     return (stdout.decode('utf-8', 'ignore'), stderr.decode('utf-8', 'ignore'))
#
#
# process = subprocess.Popen(
#     ["./random_logger.py"],
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE
# )
# stdout, stderr = kb_logger(process)
# output_value = stdout.split("\n")[0].split(" ")[-2]
#
# print(output_value)
# # count_df = pd.DataFrame(
# #     sorted(counts.items()), columns=["base", "count"]
# # )
# #
# #
# # print(output_decoded)