from flask import Flask, render_template, request, redirect, url_for
import data_handler


app = Flask(__name__)

@app.route('/')
@app.route('/list')
def list_():
    questions = data_handler.get_questions()
    header = data_handler.get_header()
    return render_template("list.html", questions=questions, header=header)


@app.route('/ask-question', methods=['POST', 'GET'])
def ask_question():
    if request.method == 'POST':
        user_storiezz = dict(request.form)
        data_handler.append_csv(user_storiezz)
        return redirect('/')

    questions = data_handler.get_questions()
    header = data_handler.get_header()
    id = data_handler.get_next_id()
    timestamp = data_handler.create_timestamp()
    return render_template('add.html', questions=questions, header=header, id=id, timestamp=timestamp)


@app.route('/question/<id>', methods=['GET', 'POST'])
def display_question(id):
    answers = data_handler.get_answers()
    questions = data_handler.get_questions()
    header = data_handler.get_header()
    answers_header = data_handler.get_answer_header()
    for num in questions:
        if num["id"] == id:
            questionz = num
    for line in answers:
        if line["question_id"] == id:
            answers = line
    return render_template('display.html', questionz=questionz, answers=answers,header=header, answers_header=answers_header)



@app.route('/question/<question_id>/new-answer', methods=['POST', 'GET'])
def add_answer(question_id):
    if request.method == 'POST':
        answer = dict(request.form)
        data_handler.append_answer_csv(answer)
        return redirect(url_for("display_question", id=question_id))
    answers = data_handler.get_answers()
    answer_id = data_handler.get_next_answer_id()
    timestamp = data_handler.create_timestamp()
    for line in answers:
        if line["id"] == question_id:
            answers = line
    return render_template('add_answer.html', answers=answers, answer_id=answer_id, timestamp=timestamp, question_id=question_id)


@app.route('/question/<id>/vote-up')
def vote_up(id):
    question
    vote_counter += 1
    return vote_counter, render_template('display.html',questions=questions, questionz=questionz, answers = answers,header=header, id=id)


@app.route('/vote-down/<question_id>')
def vote_down(question_id):
    vote_counter -= 1
    return vote_counter, redirect('question/id')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )