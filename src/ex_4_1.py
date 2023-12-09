""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def num_shutdowns(logfile):
    """
    Counts and returns the number of shutdowns present in the file.

    Args:
        logfile (str): The path to the log file.

    Returns:
        int: The number of shutdown events present in the file.
    """
    # Use the get_shutdown_events function from ex_4_0 to get shutdown entries
    shutdown_entries = get_shutdown_events(logfile)

    # Initialize a counter for the number of shutdown events
    num_shutdowns = 0

    # Iterate through the shutdown entries and count pairs of "Shutdown initiated" and "Shutdown complete"
    i = 0
    while i < len(shutdown_entries):
        if shutdown_entries[i] == "Shutdown initiated" and i + 1 < len(shutdown_entries) and shutdown_entries[i + 1] == "Shutdown complete":
            num_shutdowns += 1
            i += 2  # Move to the next pair
        else:
            i += 1  # Move to the next entry

    return num_shutdowns


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
