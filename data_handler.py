import csv, os, datetime

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'
DATA_FILE_PATH_answer = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
header = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']
DATA_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message","image"]


def get_questions():
    with open(DATA_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        questions = []
        for row in reader:
            questions.append(row)
    return questions


def get_answers():
    with open(DATA_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        answers = []
        for row in reader:
            answers.append(row)
    return answers


def append_csv(question):
    with open(DATA_FILE_PATH, "a") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=DATA_HEADER, delimiter=',')
        writer.writerow(question)


def get_next_id():
    questions = get_questions()
    id = int(questions[-1]['id']) + 1
    return id


def get_header():
    return header


def create_timestamp():
    return datetime.datetime.now().strftime('%H:%M:%S %d/%m/%Y')
