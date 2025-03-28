Hosts Blocker CLI

Overview

This is a simple Python script to block and unblock websites by modifying the /etc/hosts file. It redirects specified domains to 127.0.0.1, effectively blocking access to them. The script requires root privileges to modify system files.

Features
- Block websites by adding entries to /etc/hosts.
- Unblock websites by removing entries from /etc/hosts.
- Flush DNS cache to apply changes instantly.
