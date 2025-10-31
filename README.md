# 🧠 SysInfo CLI
*A Professional Python Command-Line System Monitor*
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?logo=linux)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 Overview
`SysInfo` is a lightweight and professional **command-line utility** that displays real-time CPU, memory, and disk usage information.
It follows *clean code principles*, modular architecture, and professional logging practice - built entirely in Python.

Developed as part of the **Elite Bootcamp 2025-2026** *(Week 1- Professional Python foundations)*, this tool demostrates how to:
- Design modular CLI programs using 'argparse'
- Apply OOP for monirtoring componets
- use structured logging with rotating file handlers
- Implement custom exceptions for user-friendly error handling

---

## ⚙️ Features
✅ Modular package structure (`models`, `utils`, `errors`)
✅ `argparse` CLI with clean help and version output
✅ Friendly error handling for invalid options
✅ PEP 8-compliant, fully type-hinted, and production-ready

---

## 🧩 Project Structure
sysinfo/
├── errors/
│ ├── init.py
│ └── exceptions.py
├── logs/
│ └── sysinfo.log
├── models/
│ ├── init.py
│ └── monitor.py
├── utils/
│ ├── init.py
│ └── utils.py
├── README.md
└── sysinfo.py

---

## 🚀 Quick start (Debian 12)
```bash
# 1. git clone https://github.com/<MichelZOGBELEMOU>/sysinfo.git
cd sysinfo

# 2. create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install psutil

# 4. Run SysInfo
python3 sysinfo.py --all
```

--- 

# 🧠 Usage Examples
```bash
# Show CPU usage only
python3 sysinfo.py --cpu

# Show memory usage 
python3 sysinfo.py --mem

# Show disk usage
python3 sysinfo.py --disk

# Show all metrics
python3 sysinfo.py --all

# Show version
 python3 sysinfo.py --version

# Example output
====== System Information ======
2025-10-31 10:44:00
CPU: 21%  | Memory: 48% | Disk: 37%

# invalid input example:
python3 sysinfo.py --cpux
#-> [error] Invalid option: --cpux
```

---

# 🪵 Logging
all activity is logged automatically:
```bash
logs/sysinfo.log
```
 with automatic rotation (max 100KB, 3 backups).
 Example:
 ```yaml
 [2025-10-31 10:44:00] INFO - System Information started
 [2025-10-31 10:44:01] INFO - System info CPU: 21% | Memory: 48% | Disk: 37%
 ```
# 👨🏿‍💻 Author
Michel Zogbelemou

📍Ulsan, South Korea

🔗https://github.com/MichelZOGBELEMOU

