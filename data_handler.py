import csv, os, datetime
import database_common
from datetime import datetime

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
