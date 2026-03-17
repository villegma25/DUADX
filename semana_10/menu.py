from typing import List, Dict
from actions import add_students, view_students, view_top_3_students, view_general_average
from data import append_to_csv, import_from_csv

def show_menu():
    students: List[Dict] = []

    while True:
        print("\n===== Student Management Menu =====")
        print("1. Add students")
        print("2. View all students")
        print("3. View top 3 students by average")
        print("4. View general average")
        print("5. Export (append) data to CSV")
        print("6. Import data from CSV")
        print("7. Exit")

        choice = input("Choose an option (1–7): ").strip()

        if choice == "1":
            students = add_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            view_top_3_students(students)
        elif choice == "4":
            view_general_average(students)
        elif choice == "5":
            if not students:
                print("\nNo students to export. Please add students first.")
            else:
                filepath = input("Enter the full path to save/append the CSV file: ").strip()
                append_to_csv(students, filepath)
        elif choice == "6":
            imported_students = import_from_csv()
            if imported_students:
                # Optionally append to current students in memory
                students.extend(imported_students)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
