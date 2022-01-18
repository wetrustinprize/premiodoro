from blessed import Terminal


def seconds_to_time(seconds: float):
    if seconds / 60 >= 1:
        if (seconds / 60) / 60 >= 1:
            hours = round((seconds / 60) / 60)

            return f"{hours} hour" + ("s" if hours > 1 else "")
        else:
            minutes = round(seconds / 60)

            return f"{minutes} minute" + ("s" if minutes > 1 else "")
    else:
        return f"{seconds} second" + ("s" if seconds > 1 else "")


class Display:
    def __init__(self):
        self.term = Terminal()

    """
    Renders the text in the terminal.

    Arguments:
        idle (bool): Tells if the user is Idle
        reminders (Reminder[]): The array with all the reminders
    """

    def main(self, idle=False, reminders=[]):
        print(self.term.clear())
        print(self.term.bold(self.term.center("Premiodoro")))

        print(self.term.center(
            "Status: " +
            (
                f"{self.term.green}Not idle"
                if not idle else
                f"{self.term.red}Idle"
            )
            + self.term.normal
        ))

        print()

        print(self.term.center(
            "Next up reminders:"
        ))

        for reminder in reminders:
            print(self.term.center(self.term.italic(
                f"{self.term.yellow}{reminder.message}{self.term.normal} in {seconds_to_time(reminder.period - reminder.passed)}"
            )))
