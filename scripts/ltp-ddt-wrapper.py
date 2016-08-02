#!/usr/bin/python

import re
import sys
import os
import subprocess

os.system('/opt/ltp/runltp -P am335x-evm -f ddt/eth_ping -s "ETH_XS_FUNC_PING" 2>&1 | tee output.txt')
os.system('/opt/ltp/runltp -P am335x-evm -f ddt/emmc_dd_rw_ext2 -s "EMMC_S_FUNC_EXT2_DD_RW_100M" 2>&1 | tee -a output.txt')

pattern = re.compile("^(?!.+ED)(?P<test_case_id>\\w+)\\s+(?P<result>PASS|FAIL)\\s+\\d+")
f = open("output.txt", "r")
try:
   for line in f:
      for parser in [pattern]:
          result = parser.search(line)
          if result is not None:
             if parser is pattern:
                test_id = result.group('test_case_id')
	        test_result = result.group('result')
                os.system('lava-test-case %s --result %s' % (test_id, test_result.lower()))
   sys.exit(0)
finally: f.close()
print "ERROR: Parser failed and ran to EOF"
sys.exit(1)
