import csv
import os
from w11_student import Student

def load_students_from_csv(filepath="w11_load_students.csv"):
    students = []

    if not os.path.exists(filepath):
        print("CSV file not found.")
        return students  # Return empty list if file is missing

    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = Student(
                name=row["name"],
                section=row["section"],
                score_1=row["score_1"],
                score_2=row["score_2"],
                score_3=row["score_3"],
                score_4=row["score_4"],
            )
            students.append(student)

    return students


def save_students_to_csv(student_list, filepath="w11_load_students.csv"):
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "section", "score_1", "score_2", "score_3", "score_4"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_list:
            writer.writerow(student.to_dict())
    print("Students saved successfully.")