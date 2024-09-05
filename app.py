from flask import Flask
from flask import request
from flask import render_template
from db.Dao import Dao

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    dao = Dao()
    dao.connect_to_db()
    data_set = dao.read_all()
    msg = "Message: \n"

    for data in data_set:
        msg += data + "\n"

    return render_template('index.html', message=msg)


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
