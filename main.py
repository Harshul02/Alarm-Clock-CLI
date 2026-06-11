import threading
import time

from alarm_service import AlarmService


def scheduler(service: AlarmService):
    while True:
        service.check_due_alarms()
        service.remove_triggered_alarms()
        time.sleep(1)


def print_help():
    print("\nAvailable Commands:")
    print("  add HH:MM       Add an alarm")
    print("  list            List active alarms")
    print("  cancel ID       Cancel an alarm")
    print("  help            Show commands")
    print("  exit            Exit application")


def main():
    service = AlarmService()

    scheduler_thread = threading.Thread(
        target=scheduler,
        args=(service,),
        daemon=True,
    )

    scheduler_thread.start()

    print("=" * 50)
    print("⏰ Alarm Clock CLI")
    print("=" * 50)

    print_help()

    while True:
        try:
            command = input("\n> ").strip()

            if not command:
                continue

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "help":
                print_help()

            elif command == "list":
                alarms = service.list_alarms()

                if not alarms:
                    print("No active alarms.")
                    continue

                print("\nActive Alarms:")

                for alarm in alarms:
                    print(
                        f"[{alarm.id}] "
                        f"{alarm.trigger_time.strftime('%Y-%m-%d %H:%M')}"
                    )

            elif command.startswith("add "):
                _, time_str = command.split(maxsplit=1)

                alarm = service.add_alarm(time_str)

                print(
                    f"Alarm [{alarm.id}] scheduled for "
                    f"{alarm.trigger_time.strftime('%Y-%m-%d %H:%M')}"
                )

            elif command.startswith("cancel "):
                parts = command.split()

                if len(parts) != 2:
                    print("Usage: cancel ID")
                    continue

                try:
                    alarm_id = int(parts[1])

                except ValueError:
                    print("Alarm ID must be a number.")
                    continue

                cancelled = service.cancel_alarm(alarm_id)

                if cancelled:
                    print(f"Alarm [{alarm_id}] cancelled.")
                else:
                    print("Alarm not found.")

            else:
                print("Unknown command.")
                print("Type 'help' to see available commands.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()