from premiodoro.reminder import Reminder
from json import load, dumps

from pynotifier import Notification
from playsound import playsound

from config import PREMIODORO_OUT


class ReminderManager:
    """
    The ReminderManager is responsible for all the reminders.
    """

    def __init__(self):
        self.reminders = []

        self.load_reminders()
        self.add_on_complete(
            lambda message: (
                playsound('./notification.wav', False),
                Notification(
                    title="Premiodoro",
                    description=message,
                    urgency='normal'
                ).send()
            )
        )

    def __iter__(self):
        return self.reminders.__iter__()

    """
    Adds a on_complete function to one or all reminders

    Arguments:
        func (callable): The function to call when reminder is complete
        index (number): The index of the reminder. Defaults: -1 (all)
    """

    def add_on_complete(self, func, index=-1):
        if index < 0:
            for reminder in self.reminders:
                reminder.on_complete(func)
        else:
            self.reminders[index].on_complete(func)

    """
    Loads the reminders.json file, reseting all the reminders
    """

    def load_reminders(self):
        with open('./reminders.json') as f:
            REMINDERS = load(f)

            self.reminders = [Reminder(
                message=reminder['message'],
                period=reminder['period']
            ) for reminder in REMINDERS]

    """
    Ticks all the reminders.

    Arguments:
        tick (number): Seconds to tick
    """

    def tick_all(self, tick=1):
        for reminder in self.reminders:
            reminder.tick(tick)
        self.update_out()

    """
    Same as tick_all() but unticks

    Arguments:
        tick (number): Seconds to untick
    """

    def untick_all(self, tick=1):
        for reminder in self.reminders:
            reminder.untick(tick)
        self.update_out()

    """
    Updates the PREMIODORO_OUT file with current information
    """

    def update_out(self):
        if PREMIODORO_OUT == None:
            return

        with open(PREMIODORO_OUT, 'w+') as file:
            self.reminders.sort(key=lambda r: r.remaining_time)

            information = {
                "next_reminder": self.reminders[0].remaining_time
            }

            file.write(dumps(information))
