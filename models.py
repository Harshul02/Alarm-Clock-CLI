from dataclasses import dataclass
from datetime import datetime

@dataclass
class Alarm:
    id: int
    trigger_time: datetime
    triggered: bool = False