from datetime import datetime, timedelta
from models import Alarm

class AlarmService:
    def __init__(self):
        self.alarms = []
        self.next_id = 1