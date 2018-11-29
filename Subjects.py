class Subjects:

    def __init__(self, amount):
        self.amount = amount

    def check_amount_of_subjects(self):
        if self.amount >= 20:
            return False
        else:
            return True
