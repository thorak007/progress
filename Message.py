import time


class Message:
    def welcome(self):
        time.sleep(1)
        print("Hello user, Welcome to Progress!")
        time.sleep(2)
        print("Lets start our work in Progress!")
        time.sleep(2)

    def message_next_step(self):
        time.sleep(1)
        print("Good! Lets start next step!")

    def message_mistake_1(self):
        time.sleep(1)
        print("Nice Joke! Try again!")

    def input_data_to_database_by_user_1(self):
        time.sleep(2)
        print("Fill subjects with marks")

    def input_data_to_database_by_user_2(self):
        time.sleep(2)
        print("Input 's' or '-' in Subject to finish filling")

    def invalid_login_password(self):
        time.sleep(1)
        print("Invalid login or password!")

    def invalid_user(self):
        time.sleep(1)
        print("Or such user have already exist!")
        time.sleep(1)
