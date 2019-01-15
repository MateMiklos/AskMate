from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    questions = data_handler.get_all_user_story()
    header = data_handler.get_header()
    return render_template("list.html", questions=questions, header=header)


@app.route('/add-question', methods=['POST', 'GET'])
def user_story():
    if request.method == 'POST':
        user_storiezz = dict(request.form)
        data_handler.append_csv(user_storiezz)
        return redirect('/')

    questions = data_handler.get_all_user_story()
    header = data_handler.get_header()
    # statuses = data_handler.get_statuses()
    # id = data_handler.get_next_id()
    return render_template('add.html', questions=questions, header=header, id=id)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
