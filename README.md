# Python TCP Scanner 🔍🐍

A custom-built TCP port scanner designed to explore the fundamentals of **Network Programming** and **Defensive Cybersecurity**. While tools like NMAP are industry standards, this project focuses on the manual implementation of socket connections and service identification (Banner Grabbing).

## Features ⚙️
- **Low-level Socket Implementation:** Uses Python's `socket` library to handle IPv4 and TCP connections.
- **Banner Grabbing:** Automatically captures service banners (SSH, FTP, SMTP) to identify the underlying daemons (More soon).
- **Protocol Probing:** Implements a specific logic for HTTP services (ports 80, 8080, 8000) by sending a manual `GET` request when no initial banner is presented.
- **Hex & Raw Output:** Displays data in hexadecimal and raw formats for deep packet inspection analysis.

## What I Learned 📝
- **TCP Three-Way Handshake:** Managing `connect_ex` to identify open vs. closed ports.
- **Timeout Management:** Implementing `settimeout` to handle network latency and unresponsive hosts.
- **Application Layer Behavior:** Understanding that "connection successful" does not always mean "data received," requiring active probing for certain protocols.

## How to use 🐍❔
1. Clone the repository.
2. Modify the `host` variable with the target IP address.
3. Run the script:
   `python main.py`

## Technologies used 🛠️
**Python 3.x 🐍** 
Native library: socket, ipaddress (no external dependencies).

## Roadmap & Future Improvements 🚧🐍

- [ ] **Concurrency:** Implement `threading` or `asyncio` to scan 65535 ports more efficiently.
    
- [ ] **Advanced Error Handling:** Deep dive into `errno` constants to differentiate between types of connection failures.
    
- [ ] **Service Mapping:** Expand the fingerprinting dictionary for more common enterprise services.

Developed as part of my journey as a Future AI & Cybersecurity Engineer. ❤️
