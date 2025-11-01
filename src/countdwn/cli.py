from countdwn.bar import Loading
import argparse
from countdwn.timeconversion import time_to_seconds


def main():

    # arg parser to get positional duration arg
    parser = argparse.ArgumentParser(description="Countdown timer with progress bar")
    parser.add_argument(
        "duration",
        nargs="?",
        default=10,
        type=str,
        help="countdown time in seconds",
    )
    args = parser.parse_args()

    # TODO: allow user to input seconds or hh:mm:ss format
    countdown_time = time_to_seconds(args.duration)

    # now make the progress bar/timer
    bar = Loading(countdown_time)
    bar.start()


if __name__ == "__main__":
    main()
