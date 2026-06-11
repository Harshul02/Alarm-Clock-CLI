from datetime import datetime, timedelta

from alarm_service import AlarmService


def test_add_alarm():
    service = AlarmService()

    alarm = service.add_alarm("23:59")

    assert alarm.id == 1
    assert len(service.alarms) == 1
    assert service.alarms[0] == alarm


def test_cancel_alarm():
    service = AlarmService()

    alarm = service.add_alarm("23:59")

    result = service.cancel_alarm(alarm.id)

    assert result is True
    assert len(service.alarms) == 0


def test_cancel_non_existent_alarm():
    service = AlarmService()

    result = service.cancel_alarm(999)

    assert result is False


def test_invalid_time_format():
    service = AlarmService()

    try:
        service.add_alarm("abc")
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_invalid_hour():
    service = AlarmService()

    try:
        service.add_alarm("25:00")
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_invalid_minute():
    service = AlarmService()

    try:
        service.add_alarm("12:60")
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_past_time_schedules_for_tomorrow():
    service = AlarmService()

    now = datetime.now()

    past_time = (now - timedelta(minutes=1)).strftime("%H:%M")

    alarm = service.add_alarm(past_time)

    assert alarm.trigger_time.date() >= now.date()

    if alarm.trigger_time.date() == now.date():
        # Handles the edge case where minute rollover happens
        assert alarm.trigger_time > now
    else:
        assert alarm.trigger_time.date() == (now + timedelta(days=1)).date()