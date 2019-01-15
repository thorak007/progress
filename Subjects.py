class Subjects:

    def __init__(self, subject, month, mark):
        self.subject = subject
        self.month = month
        self.mark = mark

    def input_marks_in_subjects(self):
        marks = []
        for i in range(12):
            marks[i] = self.mark


