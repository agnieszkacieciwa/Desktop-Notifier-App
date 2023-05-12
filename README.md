# Desktop-Notifier-App

This is a Python script that displays a desktop notification using the `plyer` library. It can be used to set up reminders or display notifications at specified intervals.

## Usage

To use the Notification Script, follow these steps:

1. Make sure you have Python installed on your system.
2. Install the `plyer` library by running the following command: `pip install plyer`.
3. Copy the script code from this repository.
4. Customize the notification settings by modifying the `title`, `message`, and `timeout` variables.
5. Run the script using the command: `python notification_script.py`.
6. The script will display a notification with the specified title and message every 30 minutes.

## Requirements

- Python 3.x
- `plyer` library

## Customization

You can customize the notification settings by modifying the following variables in the script:

```python
title = 'Notification'        # The title of the notification
message = 'Example content'   # The message body of the notification
timeout = 10                  # The duration (in seconds) for which the notification will be displayed
```
