from monitor_module import MonitorModule
from disk_space_monitor import DiskSpaceMonitor

__available_modules = {}
__available_modules["disk_space"] = DiskSpaceMonitor()


def get_module(module_name : str) -> MonitorModule:
    return __available_modules[module_name];

def get_module_list() -> list[str]:
    return __available_modules.keys()
