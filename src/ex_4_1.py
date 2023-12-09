import os
from src.ex_4_0 import get_shutdown_events
from src.ex_4_2 import logstamp_to_datetime
from src.util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")

def time_between_shutdowns(logfile):
    """
    Calculate the time between the first and last shutdown events in the given log file.

    Parameters:
    - logfile (str): The path to the log file.

    Returns:
    - timedelta: The time difference between the first and last shutdown events.
    """
    shutdown_events = get_shutdown_events(logfile)

    timestamps = [logstamp_to_datetime(event.split()[1]) for event in shutdown_events]

    return timestamps[-1] - timestamps[0]

# The code below will call your function and print the results
if __name__ == "__main__":
    result = time_between_shutdowns(FILENAME)
    print(f'Time between shutdowns: {result}')
