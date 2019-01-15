from Authorization import Authorization
from Initialization import Initialization
from DataBase import DataBase
from Message import Message


class Main:
    # Include DataBase to Progress
    d = DataBase()
    d.create_database()

    # Welcome message
    m = Message()
    m.welcome()

    # Log in
    a = Authorization()
    login = str(input('Login: '))
    password = str(input('Password: '))
    a.log_in(login, password)

    # Initialization
    i = Initialization(login)
    i.initialization_subjects()
