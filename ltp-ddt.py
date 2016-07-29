#!/usr/bin/python

import re
import sys
import os

#def results():
#   pattern = re.compile("^(?!.+ED)(?P<test_case_id>\w+)\s+(?P<result>PASS|FAIL)\s+\d+")
#   finished = 0
#   for line in sys.stdin:
#       for parser in [pattern]:
#           result = parser.search(line)
#           if result is not None:
#              if p
#                 test_result = result.group

os.system('lava-test-case test --result fail')
