import platform
import os
import sys
import json
import socket
import getpass
from datetime import datetime
from pathlib import Path


def collect_system_info():
    system_name = platform.system()

    if system_name == "Windows":
        os_name = "Windows"
    elif system_name == "Linux":
        os_name = "Linux"
    elif system_name == "Darwin":
        os_name = "macOS"
    else:
        os_name = "Неизвестная ОС"

    info = {
        "collection_time": datetime.now().astimezone().isoformat(),

        "operating_system": {
            "name": os_name,
            "system": system_name,
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.architecture()[0],
            "machine": platform.machine(),
            "processor": platform.processor()
        },
        "python": {
            "version": platform.python_version(),
            "implementation": platform.python_implementation(),
            "executable": sys.executable
        },
        "computer": {
            "hostname": socket.gethostname(),
            "username": getpass.getuser(),
            "current_directory": str(Path.cwd()),
            "home_directory": str(Path.home())
        },
        "environment": {
            "process_id": os.getpid(),
            "cpu_count": os.cpu_count(),
            "preferred_encoding": sys.getfilesystemencoding()
        },
        "network": {
            "hostname": socket.gethostname()
        }
    }

    return info

def save_to_json(data, filename="system_info.json"):
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return output_path.resolve()

def main():
    info = collect_system_info()
    output_file = save_to_json(info)
    print("Результат сохранён в файл:", output_file)

if __name__ == "__main__":
    main()