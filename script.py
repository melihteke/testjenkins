from scrapli.driver.core import IOSXEDriver

print('Hello Melih')

my_device = {
    "host": "192.168.178.1",
    "auth_username": "admin",
    "auth_password": "!mlh1985",
    "auth_strict_key": False,
}

with IOSXEDriver(**my_device) as conn:
    response = conn.send_command("show version")
