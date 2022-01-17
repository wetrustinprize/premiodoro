from blessed import Terminal
from pynput.mouse import Controller
from pynotifier import Notification

from config import REMINDERS, PREMIODORO_OUT

from premiodoro import Reminder

import lockfile
import os
import time

term = Terminal()
mouse = Controller()

# VARIABLES

# The mouse position is used to calculate if the user is in the Computer
# TODO: Maybe find a better way to check this?
last_mouse_pos = (0, 0)

# File where the Premiodoro information is stored
premio_out = None
if PREMIODORO_OUT != None:
    premio_out = open('./premiodoro', 'w+')

reminders = [Reminder(r['message'], r['period']) for r in REMINDERS]
for reminder in reminders:
    reminder.on_complete(lambda: Notification(
        title='PremioDoro Reminder',
        description=reminder.message,
        urgency='normal'
    ).send())

with lockfile.FileLock('./premiodoro', timeout=1):
    try:
        while True:
            with term.cbreak(), term.hidden_cursor():
                # print(term.clear())
                print(term.bold(term.center(" Premiodoro ")))
                print(term.center(mouse.position))

                # Waits 1 second
                time.sleep(1)

                for reminder in reminders:
                    reminder.tick(1)

    except KeyboardInterrupt:
        print(term.italic(term.center("Forced stop.")))
