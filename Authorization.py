from User import User
from Human import Human
from DataBase import DataBase
from Message import Message


class Authorization:

    def log_in(self, login, password):
        m = Message()
        d = DataBase()
        d.create_table_user()
        u = User(login, password)
        for i in range(20):
            if u.check_user_login():
                if u.check_user_password():
                    m.message_next_step()
                    u.login = login
                    u.password = password
                    break
                else:
                    m.invalid_login_password()
                    m.invalid_user()
                    login = str(input('Login: '))
                    password = str(input('Password: '))
            else:
                d.input_data_in_table_user(login, password)
                name = str(input('Name: '))
                surname = str(input('Surname: '))
                age = int(input('Age: '))
                d.create_table_human()
                d.input_data_in_table_human(login, name, surname, age)
                user = Human(name, surname, age)
                for j in range(20):
                    if user.check_age():
                        m.message_next_step()
                        break
                    else:
                        m.message_mistake_1()
                        user.age = int(input('Age: '))
                break
