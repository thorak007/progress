from Message import Message
from Human import Human
from Subjects import Subjects

# Step 1 - Welcome
m = Message()
m.welcome()

# Step 2 - Init and check_age
name = str(input('Name: '))
surname = str(input('Surname: '))
age = int(input('Age: '))

user = Human(name, surname, age)

for i in range(10):
    if user.check_age():
        m.message_next_step()
        break
    else:
        m.message_mistake_1()
        user.age = int(input('Age: '))

# Step 3 - Amount of subjects
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

# Step 4 - Init of subjects
for i in range(amount):
    m.init_subjects(i)
    subject = str(input('Subject 1: '))



