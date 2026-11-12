from datetime import datetime

SUBJECTS = [
    "Mathematics",
    "English",
    "Biology",
    "Chemistry",
    "Physics"
]

def enter_scores(student):

    print("\n===== ENTER STUDENT SCORES =====")

    scores = {}

    for subject in SUBJECTS:

        while True:
            try:
                score = float(input(f"Enter {subject} score: "))

                if 0 <= score <= 100:
                    scores[subject] = score
                    break

                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        student.scores = scores
        student.result_date = datetime.now().strftime("%d-%m-%Y")

        print("\nStudent scores recorded successfully!")

def calculate_result(student):

    if not student.scores or len(student.scores) != 5:
        print("Complete scores are not available.")
        return None

    total = sum(student.scores.values())
    average = total / 5

    if average >= 70:
        grade = "A"

    elif average >= 60:
        grade = "B"

    elif average >= 50:
        grade = "C"

    elif average >= 45:
        grade = "D"

    elif average >= 40:
        grade = "E"

    else:
        grade = "F"

    return total, average, grade

def display_result(student):

    result = calculate_result(student)

    if result is None:
        return

    total, average, grade = result

    print("/n========== STUDENT REPORT CARD ==========")
    print("Student Name:", student.full_name)
    print("STUDENT ID:", student.student_id)
    print("Class:", student.class_form)

    print("\nSUBJECT SCORES")

    for subject, score in student.scores.items():
        print(subject, ":", score)

    print("\nTotal Score:", total)
    print("Average Score:", round(average, 2))
    print("Overall Grade:", grade)
    print("Result Date:", student.result_date)

    print("===========================================")