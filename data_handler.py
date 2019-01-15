import csv
import os

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


def append_csv(new_line):
    with open(DATA_FILE_PATH, "a") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=DATA_HEADER, delimiter=';')
        writer.writerow(new_line)


def get_header():
    return header
