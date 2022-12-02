import sqlite3

conn = sqlite3.connect('SQLite_Database.db')

def sql_client(conn):
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE Client("
        "IDClient integer PRIMARY KEY,"
        "Name text,"
        "Surname text,"
        "Age integer,"
        "Phone integer)"
    )

def sql_doctor(conn):
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE Doctor("
        "IDDoctor integer PRIMARY KEY,"
        "Name text,"
        "Surname text,"
        "Specialization text,"
        "Cabinet integer,"
        "Polyclinic integer,"
        "Age integer,"
        "Phone integer)"
    )

def sql_reception(conn):
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE Doctor("
        "IDReception integer PRIMARY KEY,"
        "IDPacient integer,"
        "IDDoctor integer,"
        "DateRec integer,"
        "TimeRec integer,"
        "Cabinet integer,"
        "Diagnose integer,"
        "Price integer)"
    )

"""def sql_connection():
    try:
        con = sqlite3.connect('SQL_Exhibition')
        return con
        print("GOOD")
    except Error:
        print(Error)



#
def sql_Exhibition(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Exhibition("
        "IDExhibition integer PRIMARY KEY,"
        "Stands integer,"
        "Them text,"
        "Price integer,"
        "WholePrice integer)"
    )

    cursorObj.execute(
        "INSERT INTO Exhibition "
        "VALUES(1,1,'Тема','3456','7777')"
    )

    cursorObj.execute(
        "INSERT INTO Exhibition "
        "VALUES(2,3,'Темаf', 4444,8888)"
    )

    cursorObj.execute(
        "INSERT INTO Exhibition "
        "VALUES(3,54,'Тема3', 222,1222)"
    )
    con.commit()


def sql_Excurse(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Excurse("
        "IDExcurse integer PRIMARY KEY,"
        "IDExhibition integer,"


        "IDStand integer,"
        "Date datetime)"
    )

    cursorObj.execute(
        "INSERT INTO Excurse "
        "VALUES(1,1,1,'18.02.1999')"
    )
    cursorObj.execute(
        "INSERT INTO Excurse "
        "VALUES(2,2,2,'18.02.1998')"
    )

    con.commit()


def sql_Stand(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Stand("
        "IDStand integer PRIMARY KEY,"

        "ThemeStand text,"
        "LocalPrice integer)"
    )

    cursorObj.execute(
        "INSERT INTO Stand "
        "VALUES(1,'Nigg',222)"
    )
    cursorObj.execute(
        "INSERT INTO Stand "
        "VALUES(2,'Nigg1',222)"
    )
    cursorObj.execute(
        "INSERT INTO Stand "
        "VALUES(3,'Nigg2',232)"
    )

    con.commit()


def sql_StandMan(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE StandMan("
        "IDStandMan integer PRIMARY KEY,"
        "IDStand integer,"
        "Surname text,"
        "Firstname text,"
        "Lastname text)"
    )

    cursorObj.execute(
        "INSERT INTO StandMan "
        "VALUES(1,1,'NNN','NNN', 'NNN')"
    )

    cursorObj.execute(
        "INSERT INTO StandMan "
        "VALUES(2,2,'XXX','XXX', 'XXX')"
    )

    cursorObj.execute(
        "INSERT INTO StandMan "
        "VALUES(3,3,'EEE','EEE', 'EEE')"
    )

    con.commit()


def sql_Client(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Client("
        "IDClient integer PRIMARY KEY,"
        "Age int,"
        "Surname text,"
        "Firstname text,"
        "Lastname text)"
    )

    cursorObj.execute(
        "INSERT INTO Client "
        "VALUES(1,5,'XXX','XXX','XXX')"
    )

    cursorObj.execute(
        "INSERT INTO Client "
        "VALUES(2,6,'EEE','EEE','EEE')"
    )
    cursorObj.execute(
        "INSERT INTO Client "
        "VALUES(3,77,'X1X','X2X','X3X')"
    )

    con.commit()


def sql_ClientExcurse(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE ClientExcurse("
        "IDClient, IDExcurse integer PRIMARY KEY)"
    )

    cursorObj.execute(
        "INSERT INTO ClientExcurse "
        "VALUES(1,1)"
    )

    cursorObj.execute(
        "INSERT INTO ClientExcurse "
        "VALUES(2,2)"
    )
    cursorObj.execute(
        "INSERT INTO ClientExcurse "
        "VALUES(3,3)"
    )

    con.commit()


def select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:


        tablesList.append(tab[0])

        for listItem in tablesList:

         cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]
        print(f'table {listItem}')

    con = sql_connection()
    #sql_Exhibition(con)

    #sql_Excurse(con)


def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Stand SET ThemeStand = "Nigg" where IDStand = 1')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Stand SET ThemeStand = "Nigg1" where IDStand = 2')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Stand SET ThemeStand = "Nigg2" where IDStand = 3')
    con.commit()


def sql_delete(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE from StandMan where Firstname = "EEE" ')
    con.commit()

def sql_insert(con):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO StandMan "
        "VALUES(3,3,'EEE','EEE', 'EEE')")
    con.commit()


con = sql_connection()
#sql_insert(con)
#sql_Exhibition(con)
#sql_Excurse(con)
#sql_Stand(con)
#sql_StandMan(con)
#sql_ClientExcurse(con)
#sql_Client(con)


select(con)
#print("Обновлённая бд")
#sql_update(con)
#select(con)
#print("Бд с удалёнными полями")
#sql_delete(con)
#select(con"""
