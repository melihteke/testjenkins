from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.178.1",
    username="jenkins",
    password="jenkins",
)

output = net_connect.send_command(
    "show ip interface brief", use_textfsm=True
)
print(output)
