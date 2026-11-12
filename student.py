class Student:

    def __init__(self, student_id, full_name, class_form, gender, date_of_birth):

        self.student_id = student_id
        self.full_name = full_name
        self.class_form = class_form
        self.gender = gender
        self.date_of_birth = date_of_birth

        self.scores = {}
        self.result_date = None

    def display_info(self):

            print("\n----- STUDENT INFORMATION -----")
            print("Student ID:", self.student_id)
            print("Full Name:", self.full_name)
            print("Class:", self.class_form)
            print("Gender:", self.gender)
            print("Date of Birth:", self.date_of_birth)