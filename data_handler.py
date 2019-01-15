import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'question.csv'
DATA_FILE_PATH_answer = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'answer.csv'
DATA_HEADER = ["id","submission_time","view_number","vote_number","title","message","image"]
header = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']


def get_all_user_story():
    with open(DATA_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        questions = []
        for row in reader:
            questions.append(row)
    return questions




def get_header():
    return header