from DataBase import DataBase


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def check_user_login(self):
        d = DataBase()
        k = d.select_login_from_table_user()
        for i in range(len(k)):
            if k[i] == self.login:
                return True

    def check_user_password(self):
        d = DataBase()
        k = d.select_password_from_table_user()
        for i in range(len(k)):
            if k[i] == self.password:
                return True
