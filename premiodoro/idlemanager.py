from config import IDLE_MAXCOUNT, IDLE_USE
from pynput.mouse import Controller


class IdleManager:
    """
    The IdleManager object handles all the logic to check if the user is idle.
    """

    def __init__(self):
        self.active = True
        self.last_mouse_pos = (0, 0)
        self.total_idles = 0
        self.__mouse__ = Controller()

    """
    Returns:
        (bool): If the count is higher or equal than IDLE_MAXCOUNT
    """
    @property
    def is_idle(self):
        if not IDLE_USE:
            return False
        else:
            return self.total_idles >= IDLE_MAXCOUNT

    """
    Checks if the user is idle, if so adds to the idle counter.
    """

    def check(self):
        if not IDLE_USE:
            return

        if self.last_mouse_pos == self.__mouse__.position:
            self.total_idles += 1
        else:
            self.total_idles = 0

        self.last_mouse_pos = self.__mouse__.position
