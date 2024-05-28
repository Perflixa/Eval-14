from netmiko import ConnectHandler

# List of devices
devices = [
    {
        'device_type': 'cisco_ios',
        'host': '172.17.7.3',
        'username': 'cisco',
        'password': 'secret',
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.17.7.18',
        'username': 'cisco',
        'password': 'secret',
    },
        {
        'device_type': 'cisco_ios',
        'host': '172.17.7.4',
        'username': 'cisco',
        'password': 'secret',
    },
    {
        'device_type': 'cisco_ios',
        'host': '172.17.7.5',
        'username': 'cisco',
        'password': 'secret',
    },
        {
        'device_type': 'cisco_ios',
        'host': '172.17.7.6',
        'username': 'cisco',
        'password': 'secret',
    },
]

# List of show commands
show_commands = [
    'show ip interface',
]

# Loop through each device
for device in devices:
    # Connect to the device
    with ConnectHandler(**device) as conn:
        # Send show commands
        for command in show_commands:
            output = conn.send_command(command)
            print(f"Output of {command} on {device['host']}:\n{output}\n")