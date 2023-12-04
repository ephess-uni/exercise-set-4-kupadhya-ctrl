""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
     """
    Reads the given logfile and returns a list of lines where a shutdown was initiated.

    Args:
    - logfile (str): The path to the log file.

    Returns:
    - list: A list of lines where a shutdown was initiated.
    """
     
     shutdown_lines = []
    
     try:
        # Open the logfile and read its lines
        with open(logfile, 'r') as file:
            lines = file.readlines()
            # Iterate through each line and check if it contains "Shutdown initiated."
            for line in lines:
                if "Shutdown initiated." in line:
                    shutdown_lines.append(line.strip())
                    except FileNotFoundError:
        print(f"File not found: {logfile}")

    return shutdown_lines

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
