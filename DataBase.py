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
        cursor.execute("""CREATE TABLE IF NOT EXISTS Subjects(User Text, Subject TEXT, September TEXT, October TEXT,
                        November TEXT, December TEXT, January TEXT, February TEXT, March TEXT, April TEXT,
                        May TEXT, June TEXT, July TEXT, August TEXT) """)
        conn.commit()

    def input_data_in_table_user(self, login, password):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        user = [(login, password)]
        cursor.executemany("INSERT INTO User VALUES (?, ?)", user)
        conn.commit()

    def input_data_in_table_human(self, login, name, surname, age):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        human = [(login, name, surname, age)]
        cursor.executemany("INSERT INTO Human VALUES (?, ?, ?, ?)", human)
        conn.commit()

    def input_data_in_subjects_by_admin(self):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        progress = [('User', 'Subjects', 'September', 'October', 'November', 'December', 'January',
                    'February', 'March', 'April', 'May', 'June', 'July', 'August')]
        cursor.executemany("INSERT INTO Subjects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", progress)
        conn.commit()

    def input_data_in_subjects(self, login, subject):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        progress = [(login, subject, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')]
        cursor.executemany("INSERT INTO Subjects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", progress)
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

    def select_data_from_subject(self):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        for row in cursor.execute("SELECT * FROM Subjects"):
            print(row)

    def select_data_from_subject_test(self):
        m = []
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        a = ["Math"]
        for row in cursor.execute("SELECT * FROM Subjects WHERE Subject=?", a):
            m.append(row)
        return m

    def select_specific_data_from_table_subject(self, month, subject):
        conn = sqlite3.connect("Progress.db")
        cursor = conn.cursor()
        specific = [month, subject]
        for row in cursor.execute("SELECT ? FROM Subjects WHERE Subject=?", specific):
            print(row)
