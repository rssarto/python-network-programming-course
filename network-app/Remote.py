"""
The main purpose of this script is to dispatch a command via ssh connection through an intermediate
connection (gateway) with another machine, in this case:
local.machine -> 10.10.10.5 -> 10.10.10.2
"""
from jumpssh import SSHSession

server_session = SSHSession('10.10.10.5', 'osboxes', password='osboxes.org').open()
switch_session = server_session.get_remote_session('10.10.10.2', 'admin', password='python')
print(switch_session.get_cmd_output('show ip int brief'))
server_session.close()
