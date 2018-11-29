class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def check_age(self):
        if self.age >= 100:
            return False
        else:
            return True