from blessed import Terminal
from pynput.mouse import Controller
from pynotifier import Notification

from config import REMINDERS, PREMIODORO_OUT, IDLE_MAXCOUNT, IDLE_USE

from reminder import Reminder
from display import Display

from playsound import playsound

import lockfile
import os
import time

mouse = Controller()

# VARIABLES

# The mouse position is used to calculate if the user is in the Computer
# TODO: Maybe find a better way to check this?
last_mouse_pos = (0, 0)
total_idles = 0
def is_idle(): return total_idles >= IDLE_MAXCOUNT if IDLE_USE else False


# Check if var folder exists
if not os.path.exists('./var'):
    os.mkdir('./var')

# File where the Premiodoro information is stored
premio_out = None
if PREMIODORO_OUT != None:
    premio_out = open(PREMIODORO_OUT, 'w+')


def notf(o):
    Notification(
        title='PremioDoro Reminder',
        description=o.message,
        urgency='normal'
    ).send()


reminders = [Reminder(r['message'], r['period']) for r in REMINDERS]
for reminder in reminders:
    reminder.on_complete(
        lambda:
            playsound('./notification.wav', False)
    )

display = Display()

with lockfile.FileLock('./var/premiodoro', timeout=1):
    try:
        while True:
            with display.term.cbreak(), display.term.hidden_cursor():
                # Logic
                if last_mouse_pos == mouse.position:
                    total_idles = min(total_idles + 1, IDLE_MAXCOUNT)
                else:
                    total_idles = 0
                last_mouse_pos = mouse.position

                for reminder in reminders:
                    if is_idle():
                        reminder.untick(1)
                    else:
                        reminder.tick(1)

                # Prints
                display.main(
                    idle=is_idle(),
                    reminders=reminders
                )

                # Waits 1 second
                time.sleep(1)

    except KeyboardInterrupt:
        print(display.term.italic(display.term.center("Forced stop.")))
