import sqlite3

con = sqlite3.connect("Medicine.db")

def sql_tables(con):

    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS client("
        "id_client INTEGER PRIMARY KEY autoincrement,"
        "surname_cl TEXT,"
        "name_cl TEXT,"
        "age_cl INTEGER,"
        "phone_cl INTEGER);"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS doctor("
        "id_doctor INTEGER PRIMARY KEY autoincrement,"
        "surname_doc TEXT,"
        "name_doc TEXT,"
        "specialization_doc TEXT,"
        "cabinet INTEGER,"
        "polyclinic INTEGER,"
        "age_doc INTEGER,"
        "phone_doc INTEGER);"
    )
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS reception("
        "id_reception INTEGER PRIMARY KEY autoincrement,"
        "id_client INTEGER,"
        "id_doctor INTEGER,"
        "dateRec INTEGER,"
        "timeRec INTEGER,"
        "diagnose INTEGER,"
        "price INTEGER,"
        "FOREIGN KEY(id_client) REFERENCES client (id_client),"
        "FOREIGN KEY(id_doctor) REFERENCES doctor (id_doctor));"
    )
    con.commit()

def tables_insert(con):

    cur = con.cursor()
    cur.execute(
        "INSERT INTO client(surname_cl, name_cl, age_cl, phone_cl) VALUES"
        "('Трофимов', 'Артур', 33, 89825120099),"
        "('Макаров', 'Андрей', 35, 89825121188),"
        "('Леонов', 'Илья', 40, 88005553535),"
        "('Андреев', 'Михаил', 28, 89505230310)"
    )
    con.commit()

    cur.execute(
        "INSERT INTO doctor(surname_doc, name_doc, specialization_doc, cabinet, polyclinic, age_doc, phone_doc) VALUES"
        "('Нестерова', 'Полина', 'Аллерголог', 315, 12, 25, 89825183566),"
        "('Шувалов', 'Марк', 'Психолог', 202, 7, 27, 89825261378),"
        "('Еремеев', 'Максим', 'Стоматолог', 119, 3, 26, 89826341688),"
        "('Лебедев', 'Матвей', 'Хирург', 404, 5, 29, 89824322655)"
    )
    con.commit()

    cur.execute(
        "INSERT INTO reception(id_client, id_doctor, dateRec, timeRec, diagnose, price) VALUES"
        "(1, 3, date('2022-04-21'), time('08:00:00'), 'Удаление', 1500),"
        "(2, 4, date('2022-05-26'), time('09:00:00'), 'Грипп', 0),"
        "(3, 2, date('2022-08-07'), time('10:30:00'), 'Депрессия', 1000)"
    )
    con.commit()

def tables_update(con):

    cur = con.cursor()
    cur.execute(
        "UPDATE reception SET price = 2000 where id_client = 1"
    )
    con.commit()

    cur.execute(
        "UPDATE doctor SET name_doc = 'Ангелина' where surname_doc = 'Трофимов'"
    )
    con.commit()

    cur.execute(
        "UPDATE client SET name_cl = 'Артем' where surname_cl = 'Нестерова'"
    )
    con.commit()

def select_client(con):

    cur = con.cursor()
    cur.execute(
        "select id_client, surname_cl, name_cl, age_cl, phone_cl from client"
    )
    res = cur.fetchall()
    cur.close()
    return res

def select_doctor(con):

    cur = con.cursor()
    cur.execute(
        "select id_doctor, surname_doc, name_doc, specialization_doc, cabinet, polyclinic, age_doc, phone_doc from doctor"
    )
    res = cur.fetchall()
    cur.close()
    return res

def get_all_product_joined(con):
    cur = con.cursor()
    cur.execute(
        """select reception.id_client, reception.id_doctor, dateRec, timeRec, diagnose, price from reception
        INNER JOIN client on reception.id_client==client.id_client
        INNER JOIN doctor on reception.id_doctor==doctor.id_doctor"""
)
    res = cur.fetchall()
    cur.close()
    return res

sql_tables(con)
#tables_insert(con)
#tables_update(con)

print(select_client(con))
print(select_doctor(con))
print(get_all_product_joined(con))
con.close()
