import sys
import subprocess


# Checking IP reachability
def ip_reach(ip_list):
    for ip in ip_list:
        ip = ip.rstrip("\n")
        ping_reply = subprocess.call('ping %s -c 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()


if __name__ == "__main__":  # execute only when executing this code as a standalone application
    ip_reach(['10.10.10.2'])
