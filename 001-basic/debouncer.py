import time

class Debouncer:
    def __init__(self):
        self.last_up_time = 0
        self.last_down_time = 0

    def up(self):
        now = time.ticks_ms()
        lt = self.last_up_time
        self.last_up_time = now

        if (now - lt) < 200:
            return False
        return True

    def down(self):
        now = time.ticks_ms()
        lt = self.last_down_time
        self.last_down_time = now

        if (now - lt) < 200:
            return False
        return True
