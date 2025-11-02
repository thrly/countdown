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
        # self.in_progress = True

    def start(self) -> None:
        try:
            self._thread.start()

            # wait specified time
            time.sleep(self.user_wait_time)

            self.end()

        # on interrupt, clear and show cursor
        except KeyboardInterrupt:
            print("\r\033[?25h\r", end="", flush=True)

    def end(self) -> None:
        # self.in_progress = False
        # BUG: "\a" should be bell, check it works on different systems
        print("\r\033[?25h\r\a", end="", flush=True)

        print(f"Countdown completed ({f_secs(self.user_wait_time)})\033[K")
        # /033[K to flush end of line

        # return self.in_progress

    # calculate time remaining
    def time_remaining(self) -> float:
        time_remain = self.user_wait_time - (time.perf_counter() - self.start_time)
        return round(time_remain, 2)

    def bar(self) -> None:
        # bar length and scaling (i.e. how long a block is worth)
        # TODO: make bar_size user definable through --size arg?
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
            # TODO: check if "/033[K" will work here instead of whitespace
            print(f" {message}        \r", end="", flush=True)

            time.sleep(self.delta_increment)

        self.end()


def f_secs(seconds: int) -> str:
    # format sedonds in [hh:]mm:ss string
    hrs = int(seconds / 3600)
    seconds -= 3600 * hrs
    mins = int(seconds / 60)
    seconds -= 60 * mins

    if hrs > 0:
        time_str = f"{str(hrs).zfill(2)}:{str(mins).zfill(2)}:{str(seconds).zfill(2)}"
    else:
        time_str = f"{str(mins).zfill(2)}:{str(seconds).zfill(2)}"
    return time_str
