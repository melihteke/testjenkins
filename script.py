from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.178.1",
    username="admin",
    password="!mlh1985",
)

output = net_connect.send_command(
    "show ip arp"
)
print(output)
