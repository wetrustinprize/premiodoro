class Reminder:
    """
    The Reminder object is used the keep track of the time passed.

    Arguments:
        message (str): The reminder message to display
        period (int): Every period in seconds will display the reminder to the user
    """

    def __init__(self, message, period):
        # The reminder message
        self.message = message
        # The period
        self.period = period

        # The time passed
        self.passed = 0

        # When completed callbacks
        self.on_complete_callbacks = []

    """
    Ticks x seconds in this reminder.

    Arguments:
        seconds (int): The seconds passed. Defaults: 1
    """

    def tick(self, seconds=1):
        self.passed += seconds

        if self.passed >= self.period:
            self.passed -= self.period
            self.trigger()

    """
    Triggers the reminder, calling all functions in the on_completed_callbacks

    Arguments:
        reset_passed_time (bool): Should resets the passed time to 0? Defaults: False
    """

    def trigger(self, reset_passed_time=False):
        if reset_passed_time:
            self.passed = 0

        for func in self.on_complete_callbacks:
            func()

    """
    On complete hook.

    Arguments:
        func (function): The function that will be called when the reminder is complete (passed time reach period or trigger is called)
    """

    def on_complete(self, func):
        if callable(func):
            self.on_complete_callbacks.append(func)
        return func
