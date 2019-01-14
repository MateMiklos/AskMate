from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    header = data_handler.get_header()
    print(user_stories)
    return render_template("list.html", user_stories=user_stories, header=header)


@app.route('/story', methods=['POST', 'GET'])
def user_story():
    if request.method == 'POST':
        user_storiezz = dict(request.form)
        data_handler.append_csv(user_storiezz)
        return redirect('/')

    user_stories = data_handler.get_all_user_story()
    header = data_handler.get_header()
    # statuses = data_handler.get_statuses()
    # id = data_handler.get_next_id()
    return render_template('add.html', user_stories=user_stories, header=header, id=id)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
