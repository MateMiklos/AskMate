from flask import Flask, render_template, request, redirect, url_for
import data_handler


app = Flask(__name__)


@app.route('/')
def index():
    questions = data_handler.get_latest_questions()
    header = data_handler.get_header()
    return render_template("index.html", questions=questions, header=header)


@app.route('/list')
def list():
    questions=data_handler.get_questions()
    header = data_handler.get_header()
    return render_template("list.html", questions=questions, header=header)


@app.route("/search", methods=["POST"])
def list_():
    if request.method=="POST":
        post_request= request.form['search']
        search =('%'+post_request+'%')


@app.route("/search", methods=["GET"])
def search():
    if request.method == "GET":
        post_request = request.args.get('search')
        search = ('%' + post_request + '%')
        print(search)

    questions = data_handler.get_result_by_search(search)
    answer = data_handler.get_answer_by_search(search)
    header = data_handler.get_header()
    if answer == []:
        return render_template("search.html", questions=questions,header=header)
    return render_template("search.html", questions=answer, header=header)



@app.route('/ask-question', methods=['POST', 'GET'])
def ask_question():
    if request.method == 'POST':
        title = request.form.get('title')
        view_number = request.form.get("view_number")
        vote_number = request.form.get("vote_number", type=int)
        message = request.form.get("message")
        image = request.form.get("image")
        data_handler.insert_question_table(view_number, vote_number, title, message, image)
        return redirect('/')

    questions = data_handler.get_questions()
    header = data_handler.get_header()
    return render_template('add.html', questions=questions, header=header)


@app.route('/question/<id>', methods=['GET', 'POST'])
def display_question(id):
    answers = data_handler.get_answers_by_question_id(id)
    questions = data_handler.get_question_by_id(id)
    header = data_handler.get_header()
    answers_header = data_handler.get_answer_header()

    return render_template('display.html', questions=questions, answers=answers, header=header,
                           answers_header=answers_header)



@app.route('/question/<question_id>/new-answer', methods=['POST', 'GET'])
def add_answer(question_id):
    if request.method == 'POST':
        vote_number=request.form["vote_number"]
        message=request.form["message"]
        image=request.form["image"]
        data_handler.insert_answer_table(vote_number, question_id, message, image)
        vote_number = request.form["vote_number"]
        message = request.form["message"]
        image = request.form["image"]
        data_handler.insert_answer_table(vote_number, question_id, message, image)
        return redirect(url_for("display_question", id=question_id))

    question = data_handler.get_question_by_id(question_id)
    return render_template('add_answer.html', question=question, question_id=question_id)
    question_container = data_handler.get_questions()
    for num in question_container:
        if num["id"] == int(question_id):
            question_number = num
            print(num)
    return render_template('add_answer.html', question_number=question_number, question_id=question_id)


@app.route('/answer/<id>/new-comment', methods=['POST', 'GET'])
def comments_on_answers(id):
    answer = data_handler.get_answer_by_id(id)
    comments = data_handler.get_comments_by_answer_id(id)
    question_id = data_handler.get_question_by_id(id)
    question = data_handler.get_answers_by_question_id(id)
    header = ['Comments:']
    if request.method == 'POST':
        message = request.form["message"]
        data_handler.insert_comment_table(id, message)
        return redirect(url_for("display_question", id=question_id))
    return render_template('answer_comments.html', id=id, answer=answer, comments=comments, header=header,
                           question=question)


@app.route('/question/<id>/vote-up')
def vote_up(id):
    question
    vote_counter += 1
    return vote_counter, render_template('display.html', questions=questions, questionz=questionz, answers=answers,
                                         header=header, id=id)




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
