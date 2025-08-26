<img width="1347" height="627" alt="image" src="https://github.com/user-attachments/assets/2417a164-d051-41c9-8f34-afa49a7e5ba6" />

                                                    Advanced Vulnerability Scanner
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0-green.svg)
![Nmap](https://img.shields.io/badge/Tool-Nmap-red.svg)
![Nikto](https://img.shields.io/badge/Tool-Nikto-orange.svg)
![Nuclei](https://img.shields.io/badge/Tool-Nuclei-yellow.svg)

📌 Overview

In today’s threat landscape, where attackers constantly probe systems for weaknesses, proactive security assessment is vital. Advanced Vulnerability Scanner is a full-stack Flask-based project that brings together multiple scanning techniques in a single, intuitive web dashboard.

By integrating tools like Nmap, Nikto, and Nuclei alongside custom modules for port scanning, banner grabbing, header analysis, OS detection, and service fingerprinting, the scanner provides both breadth and depth in vulnerability assessment. Designed for controlled environments, the project demonstrates how attackers identify exposures while also emphasizing mitigation strategies and hardening practices.

✨ Features

Port Scanning → Quick (1–1024) and Full (1–65535) scans
Aggressive Scan → OS detection, service versions, default scripts
Banner Grabbing → Extract service banners from open ports
HTTP Security Header Analysis → Detect missing/insecure headers
OS Detection → Identify host operating system with accuracy levels
Service & Version Detection → Fingerprint running services
Nikto Scan → Common web server vulnerabilities & misconfigurations
Nuclei Scan → Template-based CVE & misconfiguration detection
Modern Web Dashboard → Interactive UI with copy/clear results functionality

🖥️ Tech Stack

Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Security Tools Integrated:

Nmap
 – Network scanning & service detection

Nikto
 – Web server vulnerability scanner

Nuclei
 – Template-based vulnerability scanning

Other: Python Requests, Socket, Subprocess
