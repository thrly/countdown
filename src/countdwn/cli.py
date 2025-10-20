from countdwn.bar import Loading
import argparse


def main():

    # arg parser to get positional duration arg
    parser = argparse.ArgumentParser(description="Countdown timer with progress bar")
    parser.add_argument(
        "duration",
        nargs="?",
        default=10,
        type=int,
        help="countdown time in seconds",
    )
    args = parser.parse_args()

    # TODO: allow user to input seconds or hh:mm:ss format

    # now make the progress bar/timer
    bar = Loading(args.duration)
    bar.start()


if __name__ == "__main__":
    main()
