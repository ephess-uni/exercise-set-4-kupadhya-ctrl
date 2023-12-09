""" ex_4_3.py """
import os
from datetime import timedelta

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Computes the amount of time between the first and last shutdowns in a log file.

    Args:
        logfile (str): The path to the log file.

    Returns:
        timedelta: The time difference between the first and last shutdown events.
    """
    # Get shutdown entries from the log file
    shutdown_entries = get_shutdown_events(logfile)

    # Check if there are at least two shutdown entries
    if len(shutdown_entries) < 2:
        raise ValueError("Insufficient shutdown entries to compute time difference.")

    # Convert date fields to datetime objects for the first and last shutdowns
    first_shutdown_time = logstamp_to_datetime(shutdown_entries[0].split()[1])
    last_shutdown_time = logstamp_to_datetime(shutdown_entries[-1].split()[1])

    # Compute the difference in time between the first and last shutdowns
    time_difference = last_shutdown_time - first_shutdown_time

    return time_difference


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
