from config import PREMIODORO_OUT

from premiodoro.reminder import Reminder
from premiodoro.display import Display
from premiodoro.idlemanager import IdleManager
from premiodoro.remindermanager import ReminderManager

import lockfile
import os
import time

# Check if var folder exists
if not os.path.exists('./var'):
    os.mkdir('./var')

reminders = ReminderManager()
display = Display()
idle = IdleManager()

with lockfile.FileLock('./var/premiodoro', timeout=1):
    try:
        while True:
            with display.term.cbreak(), display.term.hidden_cursor():
                # Logic
                idle.check()

                if idle.is_idle:
                    reminders.untick_all(1)
                else:
                    reminders.tick_all(1)

                # Prints
                display.main(
                    idle=idle.is_idle,
                    reminders=reminders
                )

                # Waits 1 second
                time.sleep(1)

    except KeyboardInterrupt:
        print(display.term.italic(display.term.center("Forced stop.")))
