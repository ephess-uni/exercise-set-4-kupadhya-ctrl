""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<
def high_scores(infile='scores.csv'):
    """Reads data from the input CSV file, determines the high score for each user,
    and prints the usernames and high scores in descending order.
    Args:
        infile (str): The input CSV file. Defaults to 'scores.csv'.
    Returns:
        None
    """
   # Use defaultdict to accumulate scores for each user
    user_scores = defaultdict(int)

    # Use DictReader to parse the CSV file
    with open(infile, 'r', encoding='utf-8') as file:
        reader = DictReader(file)
        for row in reader:
            username = row['username']
            score = int(row['score'])
            user_scores[username] = max(user_scores[username], score)
            # Build a list of dictionaries for high scores
    high_scores_list = [{'username': username, 'score': score} for username, score in user_scores.items()]

    # Sort the list in descending order based on score
    high_scores_list.sort(key=lambda x: x['score'], reverse=True)

    # Print the results
    for entry in high_scores_list:
        print(f"{entry['username']} {entry['score']}")
if __name__ == "__main__":
    # This main selection block will allow you to run and test
    # your solution. Press the Run button to the left of the `if`
    # statement above.
    high_scores()
