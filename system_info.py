#!/usr/bin/env python3
import subprocess
from datetime import datetime

commands = {
    "Hostname": ["hostnamectl", "--static"],
    "Uptime": ["uptime", "-p"],
    "Kernel": ["uname", "-r"],
    "CPU Cores & Load": ["nproc"],
    "Memory": ["free", "-h"],
    "Disk": ["df", "-h", "--total"],  # Added --total for a quick summary row
    "IP Address": ["ip", "-br", "addr"],
    "Failed Services": ["systemctl", "--failed", "--no-pager"],
}

print(f"=== SYSTEM HEALTH REPORT GENERATED AT: {datetime.now()} ===")

for title, command in commands.items():
    print(f"\n=== {title} ===")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )
        # Output handling: print stdout if available, otherwise stderr, stripped of trailing whitespace
        output = result.stdout.strip() if result.stdout else result.stderr.strip()
        print(output if output else "[No output returned]")
        
    except Exception as e:
        print(f"[ERROR executing {title}: {e}]")
