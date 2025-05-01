from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:marali789@localhost:5432/QA Task"
db = create_engine(db_connection_string)


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'student'


def test_select():
    connection = db.connect()
    result = connection.execute(text("select * from subject"))
    rows = result.mappings().all()
    rows1 = rows[1]
    assert rows1["subject_title"] == "Mathematics"


def test_add_subject():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        """insert into subject("subject_id", "subject_title") values (:new_id, :new_title)""")
    connection.execute(sql, {"new_id": 20, "new_title": "test_subject"})
    sql2 = text("select * from subject WHERE subject_id = :sub_id")
    result = connection.execute(sql2, {"sub_id": 20})
    rows = result.mappings().all()
    rows1 = rows[0]
    assert rows1["subject_title"] == "test_subject"
    transaction.commit()
    connection.close()


def test_update_subject():
    connection = db.connect()
    transaction = connection.begin()
    sql = text(
        """UPDATE subject SET subject_title = :update_title WHERE subject_id = :sub_id""")
    connection.execute(
        sql, {"sub_id": 20, "update_title": "test_subject2"})
    sql2 = text("SELECT subject_title FROM subject WHERE subject_id = :sub_id")
    result = connection.execute(sql2, {"sub_id": 20})
    rows = result.mappings().all()
    rows1 = rows[0]

    assert rows1["subject_title"] == "test_subject2"

    # Завершаем транзакцию и закрываем соединение
    transaction.commit()
    connection.close()


def test_delete_subject():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("""DELETE FROM subject WHERE subject_id = :sub_id""")
    connection.execute(sql, {"sub_id" : 20})
    sql2 = text("SELECT subject_title FROM subject WHERE subject_id = :sub_id")
    result = connection.execute(sql2, {"sub_id" : 20})
    rows = result.mappings().all()
    assert len(rows) == 0, "Запись не была удалена из базы данных!"
    transaction.commit()
    connection.close()
