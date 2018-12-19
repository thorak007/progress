from Subjects import Subjects
from DataBase import DataBase
from Message import Message

class Initialization:
    # Amount of Subjects
    m = Message()
    d = DataBase()
    m.message_1()
    amount = int(input('Amount: '))
    a = Subjects(amount)
    for i in range(amount):
        if a.check_amount_of_subjects():
            m.message_next_step()
            break
        else:
            m.message_mistake_1()
            amount = int(input('Amount: '))

    d.create_table_subjects()
    for i in range(amount):
        m.init_subjects(i)
        subject = str(input('Subject 1: '))
        d.input_data_in_database(subject)
