# ⏰ Alarm Clock CLI

A simple command-line alarm clock application built in Python. This project was developed as part of a software engineering exercise focused not only on implementation, but also on demonstrating engineering judgment, requirement clarification, AI-assisted development, and decision-making under ambiguity.

## Problem Statement

The assignment was intentionally open-ended: build an alarm clock as a Python CLI application without a detailed specification.

Rather than maximizing the number of features, I focused on delivering a clean, reliable, and well-structured solution while documenting the assumptions and trade-offs made during the implementation process.

---

## Features

* Set alarms using 24-hour time format (`HH:MM`)
* Support multiple active alarms
* List all scheduled alarms
* Cancel alarms by ID
* Console notification when an alarm triggers
* Terminal bell notification (`\a`)
* Automatically schedule alarms for the next day if the specified time has already passed today
* Interactive CLI experience
* Unit tests covering core functionality

---

## Assumptions

Since the requirements were intentionally ambiguous, I made the following assumptions:

* The application only needs to function while it is running.
* Alarm data does not need to persist between executions.
* A console notification is sufficient for alerting users.
* Time input should follow the 24-hour format (`HH:MM`).
* Supporting multiple alarms provides a more practical user experience.
* Simplicity and reliability are preferred over implementing advanced features within the limited exercise scope.

---

## Architecture

The application is divided into simple responsibilities:

### `models.py`

Defines the `Alarm` data model using a dataclass.

### `alarm_service.py`

Contains the business logic responsible for:

* Adding alarms
* Listing alarms
* Cancelling alarms
* Detecting and triggering due alarms

### `main.py`

Handles:

* Interactive CLI input
* Command parsing
* User feedback
* Starting the scheduler thread

### `tests/`

Contains unit tests validating the core functionality.

---

## Design Decisions

### Interactive CLI

I chose an interactive shell experience:

```
> add 18:30
> list
> cancel 1
> exit
```

instead of command-based execution because alarms exist only in memory. A stateless command approach would have made listing and cancelling alarms impractical without introducing persistence.

---

### Scheduler Implementation

#### Background Thread with Polling (**Chosen**)

**Pros**

* Simple to understand
* Uses only the standard library
* Easy to demonstrate and maintain
* Sufficient for a lightweight CLI application

**Cons**

* Polls every second, introducing minimal overhead

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Alarm-Clock-CLI
```
---

## Running the Application

Start the CLI:

```bash
python main.py
```

Example session:

```text
==================================================
⏰ Alarm Clock CLI
==================================================

> add 18:30
Alarm [1] scheduled for 2026-06-11 18:30

> list
Active Alarms:
[1] 2026-06-11 18:30

> cancel 1
Alarm [1] cancelled.

> exit
Goodbye!
```

---

## Supported Commands

### Add an alarm

```text
add HH:MM
```

Example:

```text
add 18:30
```

---

### List alarms

```text
list
```

---

### Cancel an alarm

```text
cancel ID
```

Example:

```text
cancel 2
```

---

### Display help

```text
help
```

---

### Exit the application

```text
exit
```

---

## Testing

Run the unit tests using:

```bash
pytest
```

The tests cover:

* Adding alarms
* Cancelling alarms
* Invalid input handling
* Cancelling non-existent alarms
* Scheduling past times for the following day

---

## Potential Improvements

Given additional time, I would consider implementing:

* Persistent storage
* Recurring alarms
* Snooze functionality
* Desktop notifications
* Background execution mode
* Improved command parsing using `cmd` or `argparse`
* Enhanced logging and observability
* Time zone awareness

