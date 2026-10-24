# Linux System Information Automation

A beginner homelab project that automates Linux system health checks using Python, Ansible, GitHub, and GitHub Actions.

## Current Features
- Display hostname and uptime
- Check Linux kernel version
- Review memory usage
- Check disk usage
- Display network interfaces
- Identify failed system services

## Environment
- Ubuntu 24.04 LTS
- Python 3
- Git

## Run Locally

```bash
cd /home/harith/project/SystemInfo && python3 system_info.py
cd /home/harith/project/SystemInfo && ansible-playbook -i inventory.ini playbook-SystemInfo1.yaml
cd /home/harith/project/SystemInfo/.github/workflows && vim deploy.yml
```
