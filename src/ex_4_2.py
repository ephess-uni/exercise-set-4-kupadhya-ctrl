""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    Parses the input date string and returns a datetime.datetime object.

    Args:
        datestr (str): Input date string in the format 'YYYY-MM-DDTHH:MM:SS'.

    Returns:
        datetime.datetime: A datetime object representing the parsed date and time.
    """
    # Use the datetime.strptime function to parse the date string
    date_format = '%Y-%m-%dT%H:%M:%S'
    parsed_datetime = datetime.strptime(datestr, date_format)

    return parsed_datetime


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2014-07-03T23:31:22'
    print(f'{logstamp_to_datetime(test_date)=}')
