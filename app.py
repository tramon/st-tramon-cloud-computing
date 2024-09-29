from flask import Flask, json
from flask import request, redirect
from flask import render_template
import datetime

from db.Dao import Dao

app = Flask(__name__)

dao = Dao()


@app.route("/", methods=['GET'])
def home():
    json_dataset = dao.read_top_100()
    return render_template('index.html', objects=json_dataset)


@app.route("/add", methods=['POST'])
def add():
    task_to_add = request.form['add']
    if task_to_add is not "":
        dao.insert_without_id(task_to_add)
    return redirect(request.referrer)


@app.route("/delete", methods=['POST'])
def delete():
    id_to_delete = request.form['delete']
    if id_to_delete.isdigit():
        dao.delete_by_id(id_to_delete)
    return redirect(request.referrer)


@app.route("/calendar", methods=['GET'])
def get_calendar():
    formatter = "%m/%d/%Y, %H:%M:%S"
    today_date_time = datetime.datetime.now().strftime(formatter)
    return render_template('calendar.html', date_time=today_date_time)


@app.route("/api/get", methods=['GET'])
def get_all():
    json_dataset = dao.read_top_100()
    return json_dataset


@app.route("/api/put", methods=['PUT'])
def put():
    task_to_add = request.form['put']
    if task_to_add is not "":
        dao.insert_without_id(task_to_add)
        return return_success(201)


@app.route("/api/delete", methods=['DELETE'])
def delete_via_api():
    id_to_delete = request.form['delete']
    if id_to_delete.isdigit():
        dao.delete_by_id(id_to_delete)
        return return_success()


def return_success(status_code=200):
    return json.dumps({'success': True}), status_code, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run()
