import sqlite3

class DataBase:
    def create_database(self):
        conn = sqlite3.connect("Progress.db")
        conn.commit()

    def create_table_user(self):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS User(login TEXT, password TEXT)""")
        conn.commit()

    def create_table_human(self):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Human(login TEXT, name TEXT, surname TEXT, age INTEGER)""")
        conn.commit()

    def create_table_subjects(self):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Subjects(subject TEXT, january INTEGER, february INTEGER, 
                        march INTEGER, april INTEGER, may INTEGER, june INTEGER, july INTEGER august INTEGER,
                        september INTEGER, october INTEGER, november INTEGER, december INTEGER)""")
        conn.commit()

    def input_data_in_table_user(self, login, password):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        self.user = [(login, password)]
        cursor.executemany("INSERT INTO User VALUES (?, ?)", self.user)
        conn.commit()

    def input_data_in_table_human(self, login, name, surname, age):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        self.human = [(login, name, surname, age)]
        cursor.executemany("INSERT INTO Human VALUES (?, ?, ?, ?)", self.human)
        conn.commit()

    def input_data_in_database(self, subject):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        self.progress = [(subject, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)]
        cursor.executemany("INSERT INTO Subjects VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", self.progress)
        conn.commit()

    def select_login_from_table_user(self):
        a = []
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        for row in cursor.execute("SELECT login FROM User"):
            a.append(row[0])
        return a

    def select_password_from_table_user(self):
        a = []
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        for row in cursor.execute("SELECT password FROM User"):
            a.append(row[0])
        return a