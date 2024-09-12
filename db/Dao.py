import os
from dataclasses import dataclass

import psycopg
import json
from psycopg import sql
from psycopg.rows import class_row


# Data access object
class Dao:
    dbname = os.environ.get('DB_NAME')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')

    table_name_tasks = 'tasks'
    field_id = 'id'
    field_task = 'task'

    cursor = None
    connection = None

    def __init__(self):
        Dao.connection = psycopg.connect(
            dbname=Dao.dbname,
            user=Dao.user,
            password=Dao.password,
            host=Dao.host,
            port=Dao.port
        )

    @staticmethod
    def connect_to_db():
        Dao.cursor = Dao.connection.cursor()
        Dao.cursor.row_factory = class_row(Task)
        return Dao.cursor

    @staticmethod
    def read_all(select_all_query="SELECT * FROM tasks "
                                  "ORDER BY id "
                                  "FETCH FIRST 100 ROWS WITH TIES"):
        dataset = Dao.cursor.execute(select_all_query).fetchall()
        return dataset

    @staticmethod
    def read_to_json(select_all_query="SELECT * FROM tasks "
                                      "ORDER BY id "
                                      "FETCH FIRST 100 ROWS WITH TIES"):
        dataset = json.dumps(Dao.cursor.execute(select_all_query).fetchall())
        return dataset

    @staticmethod
    def insert(task_id, task):
        query_insert_with_id = sql.SQL("INSERT INTO {table} ({fields}) VALUES (%s, %s)").format(
            table=sql.Identifier(Dao.table_name_tasks),
            fields=sql.SQL(",").join([
                sql.Identifier(Dao.field_id),
                sql.Identifier(Dao.field_task)]))
        Dao.cursor.execute(query_insert_with_id, [task_id, task])
        Dao.connection.commit()

    @staticmethod
    def insert_without_id(task):
        query_add_task = sql.SQL("INSERT INTO {table} ({field}) VALUES (%s)").format(
            table=sql.Identifier(Dao.table_name_tasks),
            field=sql.Identifier(Dao.field_task))
        Dao.cursor.execute(query_add_task, [task])
        Dao.connection.commit()

    @staticmethod
    def delete_by_id(task_id):
        query_delete_task_by_id = sql.SQL("DELETE FROM {table} WHERE {field} = %s").format(
            table=sql.Identifier(Dao.table_name_tasks),
            field=sql.Identifier(Dao.field_id))
        Dao.cursor.execute(query_delete_task_by_id, [task_id])
        Dao.connection.commit()

    @staticmethod
    def close():
        Dao.connection.close()


@dataclass
class Task:
    id: int
    task: str
