from db.Dao import Dao

dao = Dao()

if __name__ == "__main__":
    dao.connect_to_db()
    dataset = dao.read_all()
    # msg = "Message:\n"
    # for data in dataset:
    #     msg += data.__str__() + "\n"
    # print(msg)

    for t in dataset:
        k = t[0]
        v = t[1]
        print(k, v)

    dao.close()
