from flask import Flask, render_template, request, redirect
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
    for num in questions:
        if num["id"] == id:
            questionz = num
    for num in answers:
        if num["id"] == id:
            answers = num
    return render_template('display.html', questionz=questionz, answers = answers,header=header, id=id)


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