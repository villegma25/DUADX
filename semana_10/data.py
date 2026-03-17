import csv
import os
from typing import List, Dict

def append_to_csv(students: List[Dict], filepath: str) -> None:
    file_exists = os.path.exists(filepath)

    try:
        with open(filepath, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["name", "section", "spanish", "english", "social_studies", "science"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            for student in students:
                writer.writerow(student)

        print(f"\nAppended {len(students)} student(s) to '{filepath}'.")
    except Exception as e:
        print("Error appending data:", e)

def import_from_csv() -> List[Dict]:
    filepath = input("Enter the full path of the CSV file to import: ").strip()

    if not os.path.exists(filepath):
        print(f"\nFile '{filepath}' does not exist. Please check the path and try again.")
        return []

    imported_students = []
    errors = []

    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            count = 0
            for idx, row in enumerate(reader, start=2):  # start=2 for header line +1
                try:
                    student = {
                        "name": row["name"],
                        "section": row["section"],
                        "spanish": float(row["spanish"]),
                        "english": float(row["english"]),
                        "social_studies": float(row["social_studies"]),
                        "science": float(row["science"]),
                    }
                    imported_students.append(student)
                    count += 1
                except (KeyError, ValueError) as e:
                    errors.append((idx, str(e)))

        print(f"\nImported {count} student(s) from '{filepath}'.")
        if errors:
            print(f"\nSkipped {len(errors)} row(s) due to errors:")
            for line_num, error in errors:
                print(f"  Line {line_num}: {error}")
    except Exception as e:
        print("Error importing data:", e)

    return imported_students