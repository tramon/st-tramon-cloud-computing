from db.Dao import Dao

if __name__ == "__main__":
    dao = Dao()
    dao.connect_to_db()
    dataset = dao.read_all()

    msg = "Message:\n"
    for data in dataset:
        msg += data.__str__() + "\n"
    print(msg)

    dao.close()
