"""Monitor models for CPU, memory, and disk usage"""

import platform
import socket
import psutil as ps
from psutil._common import bytes2human
import utils.utils as ut


class SystemMonitor:
    """Base system monitor with host and os metadata"""

    def __init__(self) -> None:
        """Initialize a system monitoring by setting the hostname
        , the OS and the os version"""
        self.hostname = socket.gethostname()
        self.os = platform.system()
        self.os_version = ut.get_os_version()

    def __repr__(self):
        return f"System Monitoring(Hostename: {self.hostname}, OS and version: {self.os} {self.os_version})"


class CpuMonitor(SystemMonitor):
    """CPU usage monitor."""

    def __init__(self):
        """Initialize a cpu monitoring by setting the architecture and the frequence"""
        super().__init__()
        self.cpu_arch = platform.machine()
        self.cpu_frequence = ps.cpu_freq().max
        self.cpu_core_number = ps.cpu_count()

    def __repr__(self) -> str:
        return (
            super().__repr__()
            + f"CPU(Arachitecture: {self.cpu_arch}, Frequence: {self.cpu_frequence}, Number of logical cpu: {self.cpu_core_number})"
        )

    def status(self) -> dict[str:str]:
        """Return cpu usage percentage"""
        return {"cpu": ps.cpu_percent(1)}


class MemoryMonitor(SystemMonitor):
    """Memory usage monitor."""

    def __init__(self) -> None:
        super().__init__()
        self.mem_total = bytes2human(ps.virtual_memory().total)

    def __repr__(self):
        return super().__repr__() + f"Memory:{self.mem_total}"

    def status(self) -> dict[str, str]:
        """Return Memory usage percentage"""
        return {"memory": ps.virtual_memory().percent}


class DiskMonitor(SystemMonitor):
    """Disk usage percentager for the root filesystem"""

    def __init__(self) -> None:
        """Initialize a DiskMonitoring"""
        super().__init__()
        self.disk_total = bytes2human(ps.disk_usage("/").total)

    def __repr__(self):
        return super().__repr__() + f"(Disk: {self.disk_total})"

    def status(self) -> dict[str, str]:
        """Return the disk usage percentage for the root filesystem"""
        return {"disk": ps.disk_usage("/").percent}
