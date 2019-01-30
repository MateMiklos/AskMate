import csv, os, datetime
import database_common
from datetime import datetime


header = {'ID':'ID', 'Submission Time':'Submission Time', 'View Number': 'View Number', 'Vote Number':'Vote Number', 'Title':'Title', 'Message':'Message', 'Image':'Image'}
DATA_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message","image"]
answers_header = ["id","submission_time","vote_number","question_id","message","image"]
DATA_HEADER_ANSWER = ['ID', 'Submission Time','Question ID', 'Message', 'Image']

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'
DATA_FILE_PATH_answer = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
header = {'ID': 'ID', 'Submission Time': 'Submission Time', 'View Number': 'View Number', 'Vote Number': 'Vote Number',
          'Title': 'Title', 'Message': 'Message', 'Image': 'Image'}
DATA_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
answers_header = ["id", "submission_time", "vote_number", "question_id", "message", "image"]
DATA_HEADER_ANSWER = ['ID', 'Submission Time', 'Question ID', 'Message', 'Image']


@database_common.connection_handler
def get_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question;
                   """)
    questions = cursor.fetchall()
    return questions


@database_common.connection_handler
def get_answers(cursor):
    cursor.execute("""
                    SELECT * FROM answer;
    """)
    answers = cursor.fetchall()

    return answers


@database_common.connection_handler
def insert_question_table(cursor, view_number, vote_number, title, message, image):
    submission_time = datetime.now()
    cursor.execute("""INSERT INTO question(submission_time,view_number,vote_number, title,message,image)
    VALUES(%(submission_time)s,%(view_number)s,%(vote_number)s,%(title)s,%(message)s,%(image)s);
    
    """,
                   {'submission_time': submission_time, 'view_number': view_number, 'vote_number': vote_number,
                    'title': title, 'message': message, 'image': image})



@database_common.connection_handler
def insert_answer_table(cursor, vote_number, question_id, message, image):
    submission_time = datetime.now()
    cursor.execute("""INSERT INTO answer(submission_time,vote_number, question_id,message,image)
       VALUES(%(submission_time)s,%(vote_number)s,%(question_id)s, %(message)s,%(image)s);

       """,
            {'submission_time': submission_time, 'vote_number': vote_number,'question_id':question_id,'message': message, 'image': image})


                   {'submission_time': submission_time, 'vote_number': vote_number, 'question_id': question_id,
                    'message': message, 'image': image})


@database_common.connection_handler
def get_result_by_search(cursor, title):
    cursor.execute("""
                            SELECT id,submission_time, view_number, vote_number,title,message FROM question
                            WHERE title LIKE  %(title)s
                             OR message LIKE %(title)s ;
                           """,
                   {'title': title})
    result = cursor.fetchall()
    return result


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


@database_common.connection_handler
def get_answer_by_search(cursor,title):
    cursor.execute("""
                                SELECT * FROM answer
                                WHERE message LIKE  %(title)s;
                               """,
                   {'title': title})
    result = cursor.fetchall()
    return result


def get_header():
    return header


def get_answer_header():
    return DATA_HEADER_ANSWER


@database_common.connection_handler
def get_latest_questions(cursor):
    cursor.execute("""
                                SELECT * FROM question
                                ORDER BY id DESC 
                                LIMIT 5;
                               """)
    result = cursor.fetchall()
    return result


@database_common.connection_handler
def get_comments_by_answer_id(cursor, answer_id):
    cursor.execute("""
    SELECT message FROM comment
    WHERE answer_id=%(answer_id)s;
    """, {'answer_id': answer_id})
    comments = cursor.fetchall()
    return comments


@database_common.connection_handler
def get_answers_by_question_id(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE question_id=%(question_id)s;
    """, {'question_id': question_id})

    answers = cursor.fetchall()
    return answers


@database_common.connection_handler
def get_answer_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE id=%(id)s;
    """, {'id': id})

    answer = cursor.fetchall()
    return answer


@database_common.connection_handler
def get_question_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE id=%(id)s;
                   """, {'id': id})

    question = cursor.fetchall()
    return question


@database_common.connection_handler
def insert_comment_table(cursor, answer_id, message):
    submission_time = datetime.now()
    cursor.execute("""INSERT INTO comment(submission_time, answer_id, message)
       VALUES (%(submission_time)s,%(answer_id)s, %(message)s);
       """, {'submission_time': submission_time, 'answer_id': answer_id, 'message': message})

