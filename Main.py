from Message import Message
from Human import Human
from Subjects import Subjects
from DataBase import DataBase
from User import User

# Step 1 - Include DataBase to Progress
d = DataBase()
d.create_database()

# Step 2 - Welcome message
m = Message()
m.welcome()

# Step 3 - Log in
d.create_table_user()
login = str(input('Login: '))
password = str(input('Password: '))
u = User(login, password)

for i in range(10):
    if u.check_user_login(login):
        if u.check_user_password(password):
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
        for j in range(10):
            if user.check_age():
                m.message_next_step()
                break
            else:
                m.message_mistake_1()
                user.age = int(input('Age: '))
        break

# Step  - Amount of subjects
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

# Step  - Init of subjects
d.create_table_subjects()
for i in range(amount):
    m.init_subjects(i)
    subject = str(input('Subject 1: '))
    d.input_data_in_database(subject)

# Step  - Select data from database
