from abc import ABC, abstractmethod

from typing import Tuple
from typing import List

#from collector.configuration.sqlite import sqlite_config_manager
class MonitorModule(ABC):
    
    @abstractmethod
    def execute(self, cn, hostname : str, iteration_count : int) -> None:
        pass
