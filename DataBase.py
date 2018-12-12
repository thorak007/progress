import sqlite3

class DataBase:
    def create_database(self):
        conn = sqlite3.connect("Subjects.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Subjects(ID INTEGER,
                                                            Subject TEXT,
                                                            January INTEGER, 
                                                            February INTEGER, 
                                                            March INTEGER, 
                                                            April INTEGER, 
                                                            May INTEGER, 
                                                            June INTEGER, 
                                                            July INTEGER 
                                                            August INTEGER,
                                                            September INTEGER,
                                                            October INTEGER,
                                                            November INTEGER,
                                                            December INTEGER) 
                                                            """)
        conn.commit()

    def input_data_in_database(self, subject):
        conn = sqlite3.connect("Subjects.db")
        cursor = conn.cursor()
        self.progress = [(subject, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)]
        cursor.executemany("INSERT INTO Subjects VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", self.progress)
        conn.commit()

    def select_data_from_database(self):
        a = []
        conn = sqlite3.connect("Subjects.db")
        cursor = conn.cursor()
        for row in cursor.execute("SELECT rowid, * FROM Subjects"):
            a.append(row)
        return a
