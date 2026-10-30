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
cd ~/project/SystemInfo && python3 system_info.py
cd ~/project/SystemInfo && ansible-playbook -i inventory.ini playbook-SystemInfo1.yaml
cd ~/project/SystemInfo/project/SystemInfo/.github/workflows && vim deploy.yml
```
