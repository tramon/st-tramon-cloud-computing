from flask import Flask
from flask import request
from flask import render_template
from db.Dao import Dao

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html', message='A list of Tasks')


@app.route("/add", methods=['POST'])
def add():
    task = request.form['task']

    dao = Dao()
    dao.connect_to_db()
    dao.insert_without_id(task)
    dao.close()

    return f'added: , {task}'


if __name__ == "__main__":
    app.run()
