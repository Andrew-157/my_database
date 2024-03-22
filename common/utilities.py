#!/usr/bin/python3

from datetime import datetime


def raise_error(mode, user_input, time_of_error, error_reason=''):
    print(f"Time: {datetime.strftime(time_of_error, '%Y-%m-%d:%H-%M')}")
    print(f"Mode: {mode}")
    print(f"Your input: {user_input}")
    if error_reason:
        print(f"Reason of failure:")
        print(error_reason)
    print("Use 'help' command")
