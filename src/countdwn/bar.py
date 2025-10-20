import time
from threading import Thread


class Loading:
    """
    a nice loading bar to play
    """

    delta_increment = 0.2

    def __init__(self, user_wait_time) -> None:
        self._thread = Thread(target=self.bar, daemon=True)
        self.user_wait_time = user_wait_time
        self.start_time = time.perf_counter()

    def start(self):
        try:
            self._thread.start()

            # wait specified time
            time.sleep(self.user_wait_time)

            # TODO: add feedback msg at end of countdown!

            # at end, show cursor, bell and flush print
            print("\r\033[?25h\r\a", end="", flush=True)
            # BUG: "\a" should be bell, check it works...

        # on interrupt, clear and show cursor
        except KeyboardInterrupt:
            print("\r\033[?25h\r", end="", flush=True)

    # calculate time remaining
    def time_remaining(self):
        time_remain = self.user_wait_time - (time.perf_counter() - self.start_time)
        return round(time_remain, 2)

    def bar(self):
        # bar length and scaling (i.e. how long a block is worth)
        bar_size = 40
        tic_scale = self.user_wait_time / bar_size

        # hide cursor
        print("\033[?25l", end="")

        while self.time_remaining() > 0:
            print(" ", end="")
            for tic in range(bar_size):
                if tic * tic_scale < self.time_remaining():
                    print("█", end="")
                else:
                    print("░", end="")
            # append time left, then return to start of line and flush (overwrite)
            message = f"{f_secs(int(self.time_remaining() + 1))}"
            # red text for last 5 seconds
            if self.time_remaining() < 5:
                message = "\033[31m" + message + "\033[0m"

            # extra whitespave before \r to overwrite countdown when less than 1 hour
            print(f" {message}        \r", end="", flush=True)

            time.sleep(self.delta_increment)


def f_secs(seconds: int) -> str:

    hrs = int(seconds / 3600)
    seconds -= 3600 * hrs
    mins = int(seconds / 60)
    seconds -= 60 * mins

    if hrs > 0:
        time_str = f"{str(hrs).zfill(2)}:{str(mins).zfill(2)}:{str(seconds).zfill(2)}"
    else:
        time_str = f"{str(mins).zfill(2)}:{str(seconds).zfill(2)}"
    return time_str
