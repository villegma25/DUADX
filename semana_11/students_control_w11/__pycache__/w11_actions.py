from w11_student import Student


def get_valid_score(subject_name):
    while True:
        try:
            grade = float(input(f"Enter grade for {subject_name}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_student():
    name = input("Enter full name: ")
    section = input("Enter section: ")
    score_1 = get_valid_score("Spanish")
    score_2 = get_valid_score("English")
    score_3 = get_valid_score("Social Studies")
    score_4 = get_valid_score("Science")

    return Student(name, section, score_1, score_2, score_3, score_4)


def list_students(student_list):
    if not student_list:
        print("No students found.")
        return

    for i, student in enumerate(student_list, start=1):
        print(f"\nStudent {i}:")
        print(f"Name: {student.name}")
        print(f"Section: {student.section}")
        print(f"Spanish: {student.score_1}")
        print(f"English: {student.score_2}")
        print(f"Social Studies: {student.score_3}")
        print(f"Science: {student.score_4}")
        print(f"Average: { student.get_average():2f}")


def show_top_students(student_list):
    if len(student_list) < 1:
        print("No students found.")
        return
    
    sorted_students = sorted(student_list, key=lambda s: s.get_average(), reverse=True)
    top_n = min(3, len(sorted_students))

    print(f"\nTop { top_n} Students:")
    for i in range(top_n):
        student = sorted_students[i]
        print(f"{i + 1}. {student.name} - Average: {student.get_average():.2f}")
        

def show_class_average(student_list):
    if len(student_list) < 1:
        print("No data found.")
        return

    total = sum(s.get_average() for s in student_list)
    class_general_average = total / len(student_list)

    print(f"General average of all students: {class_general_average:.2f}")