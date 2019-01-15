import csv
import os
import datetime

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'question.csv'
DATA_FILE_PATH_answer = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'answer.csv'
header = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']


def get_questions():
    with open(DATA_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        questions = []
        for row in reader:
            questions.append(row)
    return questions


def get_header():
    return header


def append_csv(question):
    with open('AskMate/sample_data/question.csvs') as csv_questions:
        writer = csv.writer(csv_questions)
        writer.writerows(question)


def id_generator():
    pass


def create_timestamp():
    return datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S %d:%m:%Y')
