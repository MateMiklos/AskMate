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
    # statuses = data_handler.get_statuses()
    # id = data_handler.get_next_id()
    return render_template('add.html', questions=questions, header=header, id=id)

@app.route('/question/<question_id>')
def display_question():
    questions = data_handler.get_questions()
    header = data_handler.get_header()
    return render_template('display.html', questions=questions, header=header, question_id=question_id)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
