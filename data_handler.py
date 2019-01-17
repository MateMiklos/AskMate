import csv, os, datetime

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'
DATA_FILE_PATH_answer = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
header = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']
DATA_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message","image"]
answers_header = ["id","submission_time","vote_number","question_id","message","image"]
DATA_HEADER_ANSWER = ['ID', 'Submission Time','Question ID', 'Message', 'Image']


def get_questions():
    with open(DATA_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        questions = []
        for row in reader:
            questions.append(row)
    return questions


def get_answers():
    with open(DATA_FILE_PATH_answer) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        answers = []
        for row in reader:
            answers.append(row)
    return answers


def append_csv(question):
    with open(DATA_FILE_PATH, "a") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=DATA_HEADER, delimiter=',')
        writer.writerow(question)


def append_answer_csv(answer):
    with open(DATA_FILE_PATH_answer, "a") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=answers_header, delimiter=',')
        writer.writerow(answer)

def get_next_id():
    questions = get_questions()
    id = int(questions[-1]['id']) + 1
    return id

def get_next_question_id():
    questions = get_answers()
    question_id = int(questions[-1]['id']) + 20
    return question_id



def get_next_answer_id():
    answers= get_answers()
    answer_id = int(answers[-1]['id']) + 1
    return answer_id




def get_header():
    return header

def get_answer_header():
    return DATA_HEADER_ANSWER


def id_generator():
    pass


def create_timestamp():
    return datetime.datetime.now().strftime('%H:%M:%S %d/%m/%Y')



def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'