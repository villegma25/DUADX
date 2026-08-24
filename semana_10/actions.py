from typing import List, Dict

def get_valid_grade(subject_name: str) -> float:
    while True:
        try:
            grade = float(input(f"Enter grade for {subject_name}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_students(students: List[Dict]) -> List[Dict]:
    while True:
        try:
            n = int(input("How many students do you want to add? "))
            if n > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for i in range(n):
        print(f"\nStudent #{i + 1}")
        student = {
            "name": input("Enter full name: ").strip(),
            "section": input("Enter section (e.g., 11B): ").strip(),
            "spanish": get_valid_grade("Spanish"),
            "english": get_valid_grade("English"),
            "social_studies": get_valid_grade("Social Studies"),
            "science": get_valid_grade("Science"),
        }
        students.append(student)

    return students

def view_students(students: List[Dict]) -> None:
    if not students:
        print("\nNo students found.")
        return

    print("\nList of Students:\n" + "-"*30)
    for i, student in enumerate(students, start=1):
        print(f"Student #{i}")
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish']}")
        print(f"English: {student['english']}")
        print(f"Social Studies: {student['social_studies']}")
        print(f"Science: {student['science']}")
        print("-" * 30)

def calculate_average(student: Dict) -> float:
    return (student["spanish"] + student["english"] + student["social_studies"] + student["science"]) / 4

def view_top_3_students(students: List[Dict]) -> None:
    if not students:
        print("\nNo students found.")
        return

    students_with_avg = [
        {
            "name": s["name"],
            "section": s["section"],
            "average": calculate_average(s)
        }
        for s in students
    ]

    top_students = sorted(students_with_avg, key=lambda s: s["average"], reverse=True)

    print("\nTop 3 Students by Average Grade:\n" + "-" * 40)
    for i, student in enumerate(top_students[:3], start=1):
        print(f"#{i} {student['name']} ({student['section']}) - Avg: {student['average']:.2f}")

def view_general_average(students: List[Dict]) -> None:
    if not students:
        print("\nNo students found.")
        return

    total = sum(calculate_average(s) for s in students)
    general_avg = total / len(students)

    print(f"\nGeneral average of all students: {general_avg:.2f}")
