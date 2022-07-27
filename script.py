from nike_devices import NikeCiscoDevice

device = NikeCiscoDevice("192.168.178.1", "admin", "!mlh1985")
device.get_chassis_info()
print(device.get_chassis_info())
