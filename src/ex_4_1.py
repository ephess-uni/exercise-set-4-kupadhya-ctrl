""" ex_4_1.py """
import os
from src.ex_4_0 import get_shutdown_events
from src.util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')

def num_shutdowns(logfile):
    """
    Count and return the number of shutdown events in the given log file.

    Parameters:
    - logfile (str): The path to the log file.

    Returns:
    - int: The number of shutdown events in the log file.
    """
    shutdown_events = get_shutdown_events(logfile)
    return len(shutdown_events)

# The code below will call your function and print the results
if __name__ == "__main__":
    shutdown_count = num_shutdowns(FILENAME)
    print(f'Number of shutdown events: {shutdown_count}')
