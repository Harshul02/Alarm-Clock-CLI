from datetime import datetime, timedelta
from models import Alarm


class AlarmService:
    def __init__(self):
        self.alarms = []
        self.next_id = 1

    def add_alarm(self, time_str: str) -> Alarm:
        """
        Add an alarm in HH:MM format.
        If the time has already passed today, schedule it for tomorrow.
        """
        try:
            hour, minute = map(int, time_str.split(":"))

            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError()

        except ValueError:
            raise ValueError("Invalid time format. Use HH:MM (24-hour format).")

        now = datetime.now()

        trigger_time = now.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0,
        )

        if trigger_time <= now:
            trigger_time += timedelta(days=1)

        alarm = Alarm(
            id=self.next_id,
            trigger_time=trigger_time,
        )

        self.alarms.append(alarm)
        self.next_id += 1

        return alarm

    def list_alarms(self):
        return sorted(self.alarms, key=lambda a: a.trigger_time)

    def cancel_alarm(self, alarm_id: int) -> bool:
        for alarm in self.alarms:
            if alarm.id == alarm_id:
                self.alarms.remove(alarm)
                return True

        return False

    def check_due_alarms(self):
        now = datetime.now()

        for alarm in self.alarms:
            if not alarm.triggered and now >= alarm.trigger_time:
                alarm.triggered = True

                print("\n" + "=" * 40)
                print("\a🔔 ALARM!")
                print(
                    f"Alarm {alarm.id} triggered at "
                    f"{alarm.trigger_time.strftime('%H:%M')}"
                )
                print("=" * 40)

    def remove_triggered_alarms(self):
        self.alarms = [
            alarm for alarm in self.alarms
            if not alarm.triggered
        ]