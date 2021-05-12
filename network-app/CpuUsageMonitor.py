import sys
import time

from ip.ip_reach import ip_reach
from ip.ip_file_validity import ip_file_valid
from ip.ip_addr_valid import ip_addr_valid
from ssh.ssh_connection_cpu_usage import ssh_connection
from threads.create_threads import create_threads

# Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

# Verifying the validity of each IP address in the file
try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# Calling threads creation function for one or multiple SSH connections
while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(10)
