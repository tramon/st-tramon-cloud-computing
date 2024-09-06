from flask import Flask, jsonify
from flask import request, redirect
from flask import render_template
from db.Dao import Dao

app = Flask(__name__)

dao = Dao()


@app.route("/", methods=['GET'])
def home():
    dao.connect_to_db()
    dataset = dao.read_all()
    return render_template('index.html', objects=dataset)


@app.route("/get", methods=['GET'])
def get():
    dao.connect_to_db()
    dataset = dao.read_all()
    return jsonify(dataset)


@app.route("/add", methods=['POST'])
def add():
    task_to_add = request.form['add']
    if task_to_add is not "":
        dao.connect_to_db()
        dao.insert_without_id(task_to_add)
    return redirect(request.referrer)


@app.route("/delete", methods=['POST'])
def delete():
    id_to_delete = request.form['delete']
    if id_to_delete.isdigit():
        dao.connect_to_db()
        dao.delete_by_id(id_to_delete)
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run()
