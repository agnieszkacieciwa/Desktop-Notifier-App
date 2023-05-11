from plyer import notification
import time

# Notification settings
title = 'Notification'
message = 'Example notification content'
timeout = 10

# Infinite loop that displays a notification every 30 min
while True:
    notification.notify(title=title, message=message, timeout=timeout)
    time.sleep(1800)
