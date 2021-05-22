"""
With the command below is possible to execute this python script remotely
through a gateway machine. In this case we have the following structure:
local.machine -> gateway (10.10.10.5) -> target (10.10.10.2)
cat ping_script.py | ssh osboxes@10.10.10.5 python3
"""

import subprocess
import sys

ip = '10.10.10.2'

ping_reply = subprocess.call('ping %s -c 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                             shell=True)
if ping_reply == 0:
    print("\n* {} is reachable :)\n".format(ip))
else:
    print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
    sys.exit()
