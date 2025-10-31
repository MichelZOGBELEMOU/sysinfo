"""Main entry point for SysInfo CLI tool
Provides cpu, memory, disk usage with clean logging and friendly errors"""

import argparse as ap
import sys
from datetime import datetime
from pathlib import Path
import models.monitor as m
import utils.utils as ut
import errors.exceptions as er

# Configuration
LOG_FILE: str = "logs/sysinfo.log"
MAX_FILE_SIZE_BYTES: int = 100 * 1024  # 100KB
BACKUP_FILE_COUNT: int = 3
APP_VERSION: str = "SysInfo v1.0"
PROGRAM_NAME: str = "sysinfo.py"


def main() -> None:
    """The program entry point"""

    # Create the instances of Monitor
    cpu = m.CpuMonitor()
    memory = m.MemoryMonitor()
    disk = m.DiskMonitor()

    # Create an argument parser object
    parser = er.CustomParser(
        prog=PROGRAM_NAME,
        description="Print CPU, Memory, and Disk usage information",
        epilog="tip: use --all to print everything at once",
    )
    # Add arguments to the parser
    parser.add_argument(
        "--cpu", help="Print the cpu usage in percentage", action="store_true"
    )
    parser.add_argument(
        "--mem", help="Print the memory usage in percentage", action="store_true"
    )
    parser.add_argument(
        "--disk", help="Print the disk usage in percentage", action="store_true"
    )
    parser.add_argument(
        "--all", help="Print all the monitoring of the system", action="store_true"
    )
    parser.add_argument("--version", action="version", version="Sysinfo v1")

    # Create a log file if does'nt exist
    file = Path(LOG_FILE)
    file.parent.mkdir(parents=True, exist_ok=True)

    # Create a logger
    logger = ut.get_logging(
        file, maxbytes=MAX_FILE_SIZE_BYTES, backupcount=BACKUP_FILE_COUNT
    )
    print("======System Information=======")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(cpu)
    logger.info("======System Information started =======")
    logger.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logger.info(cpu)
    # parsing arguments
    try:
        args = parser.parse_args()
    except er.InvalidOptionError as e:
        print(e)
        logger.error(f"Error during execution {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)
    logger.info(f"Command executed {vars(args)}")

    try:
        result = []
        if args.all or args.cpu:
            message = f"CPU: {cpu.status()['cpu']}%"
            print(message)
            result.append(message)
        if args.all or args.mem:
            message = f"Memory: {memory.status()['memory']}%"
            print(message)
            result.append(message)
        if args.all or args.disk:
            message = f"Disk: {disk.status()['disk']}%"
            result.append(message)
            print(message)

        output = " | ".join(result)
        logger.info(f"System info: {output}")
        logger.info(f"Sysinfo executed successfully.\n")
    except Exception as e:
        logger.error(f"Error during execution: {e}", exc_info=True)
        print(f"Error {e}")


if __name__ == "__main__":
    main()
