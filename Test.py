from DataBase import DataBase
d = DataBase()
#d.create_database()
#d.create_table_subjects()
#month = "September"
subject = 'Math'
login = 'thorak007'
#d.input_data_in_subjects_by_admin()
#d.input_data_in_subjects(login, subject)
#d.select_data_from_subject()
#d.select_specific_data_from_table_subject(month, subject)
l = d.select_data_from_subject_test()
print(l)
l.remove(l[0][0])
print(l)
