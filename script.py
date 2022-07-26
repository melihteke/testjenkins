
from scrapli.driver.core import IOSXEDriver

print('Hello Jenkins')

my_device = {
    "host": "172.18.0.11",
    "auth_username": "scrapli",
    "auth_password": "scrapli",
    "auth_strict_key": False,
}

with IOSXEDriver(**my_device) as conn:
    response = conn.send_command("show version")
