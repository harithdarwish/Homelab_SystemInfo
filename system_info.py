#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

commands = {
    "System Details": ["hostnamectl"],
    "CPU Cores & Load": ["nproc"],
    "Uptime": ["uptime", "-p"],
    "Disk i/o": ["iostat", "-x"],
    "Memory": ["free", "-h"],
    "Block Devices": ["lsblk"],
    "Disk": ["df", "-h", "--total"],
    "IP Address": ["ip", "-br", "addr"],
    "Listening Ports": ["ss", "-tulpn"],
    "Failed Services": ["systemctl", "--failed", "--no-pager"],
}

# Grab the custom run note from the environment (defaults to standard check if run locally)
run_note = os.environ.get("RUN_NOTE", "Local Execution / Routine System Check")

print(f"=== SYSTEM HEALTH REPORT GENERATED AT: {datetime.now()} ===")
print(f"=== RUN NOTE: {run_note} ===")

for title, command in commands.items():
    print(f"\n=== {title} ===")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )
        output = result.stdout.strip() if result.stdout else result.stderr.strip()

        # Filter hostnamectl output to keep only the requested lines
        if title == "System Details" and output:
            allowed_keys = ("Static hostname:", "Operating System:", "Kernel:", "Architecture:", "Firmware Age:")
            filtered_lines = [
                line.strip() for line in output.splitlines()
                if line.strip().startswith(allowed_keys)
            ]
            output = "\n".join(filtered_lines)

        print(output if output else "[No output returned]")

    except Exception as e:
        print(f"[ERROR executing {title}: {e}]")
