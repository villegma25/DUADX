from w11_actions import create_student, list_students, show_top_students, show_class_average
from w11_data import save_students_to_csv, load_students_from_csv

def show_menu():
    students = []

    while True:
        print("\n===== Student Management Menu =====")
        print("1. Add student")
        print("2. View all students")
        print("3. View top 3 students by average")
        print("4. View general average")
        print("5. Export (append) data to CSV")
        print("6. Import data from CSV")
        print("7. Exit")

        choice = input("Choose an option (1–7): ").strip()

        if choice == "1":
            student = create_student()
            students.append(student)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            show_top_students(students)
        elif choice == "4":
            show_class_average(students)
        elif choice == "5":
            if not students:
                print("No students to export.")
            else:
                path = input("Enter path to save CSV: ")
                save_students_to_csv(students, path)
        elif choice == "6":
            path = input("Enter path to load CSV: ")
            students = load_students_from_csv(path)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    show_menu()
