import subprocess

commands = {
    "Hostname": ["hostnamectl", "--static"],
    "Uptime": ["uptime", "-p"],
    "Kernel": ["uname", "-r"],
    "Memory": ["free", "-h"],
    "Disk": ["df", "-h"],
    "IP Address": ["ip", "-br", "addr"],
    "Failed Services": ["systemctl", "--failed", "--no-pager"],
}

for title, command in commands.items():
    print(f"\n=== {title} ===")
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    print(result.stdout or result.stderr)
