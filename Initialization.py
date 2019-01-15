from Subjects import Subjects
from DataBase import DataBase
from Message import Message


class Initialization:
    def __init__(self, login):
        self.login = login

    def initialization_subjects(self):
        m = Message()
        m.input_data_to_database_by_user_1()
        m.input_data_to_database_by_user_2()
        s = Subjects()
        for i in range(20):
            subject = str(input('Subject: '))
            if subject == "s":
                break
            elif subject == "-":
                break