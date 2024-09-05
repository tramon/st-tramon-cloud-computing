from flask import Flask
from flask import request
from flask import render_template
from db.Dao import Dao

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    dao = Dao()
    dao.connect_to_db()
    dataset = dao.read_all()

    msg = "Message:\n"
    for data in dataset:
        msg += data.__str__() + "\n"

    return render_template('index.html', message=msg)


@app.route("/add", methods=['POST'])
def add():
    task = request.form['task']

    dao = Dao()
    dao.connect_to_db()
    dao.insert_without_id(task)
    dao.close()


if __name__ == "__main__":
    app.run()
