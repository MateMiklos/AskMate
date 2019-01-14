import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'question.csv'
DATA_HEADER = ["id","submission_time","view_number","vote_number","title","message","image"]
header = ['ID', 'Title', 'User Story', 'Acceptance Criteria', 'Business Value', 'Estimation', 'Status']


def get_all_user_story():
    with open(DATA_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        user_stories = []
        for row in reader:
            user_stories.append(row)
    return user_stories




def get_header():
    return header