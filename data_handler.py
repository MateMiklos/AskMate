import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'question.csv'
DATA_FILE_PATH_answer = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'answer.csv'
header = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']
DATA_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message,image"]


def get_questions():
    with open(DATA_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        questions = []
        for row in reader:
            questions.append(row)
    return questions


def append_csv(question):
    with open(DATA_FILE_PATH, "a") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=DATA_HEADER, delimiter=';')
        writer.writerow(question)


def get_header():
    return header


def id_generator():
    pass


def create_timestamp():
    return datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S %d:%m:%Y')
