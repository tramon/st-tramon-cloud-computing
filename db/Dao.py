import psycopg


class Dao:
    dbname = "tramonpostgresdb"
    user = "admin"
    password = "ucslxW6OUGlZEe9RLzAckFlbb6stDih9"
    host = "dpg-crc0cdd6l47c73d9spm0-a.frankfurt-postgres.render.com"
    port = "5432"

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
        return Dao.cursor

    @staticmethod
    def read_all(select_all_query="SELECT * FROM tasks"):
        dataset = Dao.cursor.execute(select_all_query).fetchall()
        return dataset

    @staticmethod
    def insert(id, task):
        insert_query_mask = "INSERT INTO public.tasks (id, task) VALUES ({0}, '{1}')"
        insert_query = insert_query_mask.format(id, task)
        Dao.cursor.execute(insert_query)
        Dao.connection.commit()

    @staticmethod
    def insert_without_id(task):
        insert_query_without_id_mask = "INSERT INTO public.tasks (task) VALUES ('{0}')"
        insert_query = insert_query_without_id_mask.format(task)
        Dao.cursor.execute(insert_query)
        Dao.connection.commit()

    @staticmethod
    def delete_by_id(id):
        delete_query_mask = "DELETE FROM tasks WHERE id = {0}"
        delete_query = delete_query_mask.format(id)
        Dao.cursor.execute(delete_query)
        Dao.connection.commit()

    @staticmethod
    def close():
        Dao.connection.close()
