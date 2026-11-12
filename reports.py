from pathlib import Path
from results import calculate_result

def save_student_report(student):

    result = calculate_result(student)

    if result is None:
        print("This student does not have complete scores.")
        return

    total, average, grade = result

    report_folder = Path(__file__).parent / "reports"
    report_folder.mkdir(exist_ok=True)

    filename = f"{student.student_id}_report.txt"
    report_path = report_folder / filename

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("STUDENT RESULT REPORT\n")
        file.write("============================\n")
        file.write(f"Student Name: {student.full_name}\n")
        file.write(f"Student ID: {student.student_id}\n")
        file.write(f"Class: {student.class_form}\n")
        file.write(f"Gender: {student.gender}\n")

        file.write("\nSUBJECT SCORES\n")

        for subject, score in student.scores.items():
            file.write(f"{subject}: {score}\n")

        file.write(f"\nTotal Score: {total}\n")
        file.write(f"Average Score: {average:.2f}\n")
        file.write(f"Overall Grade: {grade}\n")
        file.write(f"Result Date: {student.result_date}\n")

    print("\nReport generated successfully!")
    print("Saved at:", report_path)


def calculate_class_statistics(students):

    students_with_results = []

    for student in students:
        result = calculate_result(student)

        if result is not None:
            total, average, grade = result
            students_with_results.append((student, average))

        if not students_with_results:
            print("No student results available.")
            return

        highest = max(students_with_results, key=lambda x: x[1])
        lowest = min(students_with_results, key=lambda x: x[1])

        class_average = sum(
            average for student, average in students_with_results
        ) / len(students_with_results)

        print("\n===== CLASS STATISTICS ======")

        print("Number of students with results:", len(students_with_results))

        print("Highest Average:", highest[1])
        print("Student", highest[0].full_name)

        print("Lowest Average:", lowest[1])
        print("Student:", lowest[0].full_name)

        print("Overall Class Average:", round(class_average, 2))

        print("=======================")