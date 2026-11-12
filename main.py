from student import Student
from datetime import datetime
import json
from pathlib import Path
from results import enter_scores, display_result
from reports import save_student_report, calculate_class_statistics


DATA_FILE = Path(__file__).parent /"data" / "students.json"


students = []


def save_students():

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    student_data = []

    for student in students:
        student_data.append({
            "student_id": student.student_id,
            "full_name": student.full_name,
            "class_form": student.class_form,
            "gender": student.gender,
            "date_of_birth": student.date_of_birth,
            "scores": student.scores,
            "result_date": student.result_date
        })

    with open(DATA_FILE, "w") as file:
        json.dump(student_data, file, indent=4)

    print("Student records saved successfully!")
    print("File location:", DATA_FILE.resolve())
    print("Number of students saved:", len(student_data))


def load_students():

    global students

    if not DATA_FILE.exists():
        students = []
        return

    try:
        with open(DATA_FILE, "r") as file:
            student_data = json.load(file)

        students = []

        for item in student_data:

            student = Student(
                item["student_id"],
                item["full_name"],
                item["class_form"],
                item["gender"],
                item["date_of_birth"]
            )

            student.scores = item.get("scores", {})
            student.result_date = item.get("result_date")

            students.append(student)

        print(len(students), "existing students loaded successfully.")

    except (json.JSONDecodeError, KeyError, TypeError) as error:
        print("could not load student records:", error)
        students = []

    
def register_student():

    print("\n===== REGISTER NEW STUDENT =====")

    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    class_form = input("Enter Class/Form: ")
    gender = input("Enter Gender: ")

    date_of_birth = input("Enter Date of Birth (DD-MM-YYYY):  ")

    try:
        datetime.strptime(date_of_birth, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return

    new_student = Student(
        student_id,
        full_name,
        class_form,
        gender,
        date_of_birth
    )

    students.append(new_student)

    save_students()

    print("\nStudent registered successfully!")



def view_students():

    print("\n===== REGISTERED STUDENTS =====")

    if not students:
        print("No students registered yet.")
        return

    for student in students:
        student.display_info()

def search_student():

    print("\n===== SEARCH STUDENTS =====")

    search_value = input("\nEnter Student ID or Name:").strip().lower()

    if not search_value:
        print("Please enter a student ID or Name")

    found = False

    for student in students:

        student_id = student.student_id.strip().lower()
        student_name = student.full_name.strip().lower()

        if search_value == student_id or search_value in student_name:

           print("\nStudent found!")
           student.display_info()
           found = True
           break

    if not found:
        print("Student not found.")

def update_student():

    student_id = input("\nEnter Student ID to update: ")

    for student in students:

        if student.student_id == student_id:

            print("\nStudent found!")
            student.display_info()

            print("/nEnter new information.")
            print("Press Enter to keep existing information.")

            new_name = input("New Full Name: ")
            new_class = input("New Class/Form: ")
            new_gender = input("New Gender: ")
            new_dob = input("New Date of Birth: ")

            if new_name:
                student.full_name = new_name

            if new_class:
                student.class_form = new_class

            if new_gender:
                student.gender = new_gender

            if new_dob:
                try:
                    datetime.strptime(new_dob, "%d-%m-%Y")
                    student.date_of_birth = new_dob
                except ValueError:
                    print("Invalid date format.")

            print("Student information updated successfully!")
            return
        print("Student not found.")


def delete_student():

    student_id = input("\nEnter Student ID to delete: ")

    for student in students:

        if student.student_id == student_id:

            student.display_info()

            confirmation = input(
                "Are you sure you want to delete this student? (yes/no): "
            )

            if confirmation.lower() == "yes":
                students.remove(student)
                print("Student deleted sucessfully")
            else:
                print("Deletion cancelled")

            return
    print("Student not found.")


def add_student_scores():

    print("\n===== ENTER STUDENT SCORES =====")

    student_id = input("\nEnter Student ID:  ").strip()

    print("Searching for:", student_id)

    found = False

    for student in students:

        print("Checking ID:", student.student_id)

        if student.student_id.lower() == student_id.lower():

            print("\nStudent found!")
            print("Name:", student.full_name)

            enter_scores(student)
            save_students()

            found = True
            break
    if not found:
        print("\nStudent not found. Check the student ID and try again.")

        

def view_student_result():

    student_id = input("\nEnter Student ID:  ").strip()

    for student in students:

        if student.student_id.lower() == student_id.lower():

            display_result(student)

            return

        print("Student not found.")


def generate_student_report():
    student_id = input("\nEnter Student ID: ").strip()

    for student in students:
        if student.student_id.lower() == student_id.lower():
            save_student_report(student)
            return

    print("Student not found.")

def view_class_statistics():
    calculate_class_statistics(students)



load_students()

print("Students loaded:", len(students))
print("JSON file location:", DATA_FILE.resolve())

while True:

    print("\n=====STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Register Students")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Update Students")
    print("5. Delete Students")
    print("6. Enter student scores")
    print("7. View student Result")
    print("8. Generate Student Report")
    print("9. View Class Statistics")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        print("Option 2 selected")
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        add_student_scores()

    elif choice == "7":
        view_student_result()

    elif choice == "8":
        generate_student_report()

    elif choice == "9":
        view_class_statistics()

    elif choice == "10":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice.please try again.")


