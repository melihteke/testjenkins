from netmiko import ConnectHandler
from pprint import pprint

net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.178.1",
    username="jenkins",
    password="jenkins",
)

output = net_connect.send_command(
    "show version", use_textfsm=True
)
pprint(output)
