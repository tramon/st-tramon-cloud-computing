from flask import Flask, request
from db.Dao import Dao

app = Flask(__name__)

dao = Dao()


@app.route("/api/put", methods=['PUT'])
def put():
    task_to_add = request.form['put']
    if task_to_add is not "":
        dao.connect_to_db()
        dao.insert_without_id(task_to_add)
        dao.close()


@app.route("/api/delete", methods=['DELETE'])
def delete():
    id_to_delete = request.form['delete']
    if id_to_delete.isdigit():
        dao.connect_to_db()
        dao.delete_by_id(id_to_delete)
        dao.close()
