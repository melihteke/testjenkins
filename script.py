from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.178.1",
    username="jenkins",
    password="jenkins",
)

output = net_connect.send_command(
    "show ip nat translations", use_textfsm=True
)
print(output)
