notes = 0
approved_grades  = 0
failed_grades = 0
average_approved = 0 
average_failed = 0
average_grades_t = 0
notes_counter = 1
note_a = 0 
notes_a_t = 0
notes_f_t = 0
notes_t = 0

notes = int(input("Ingrese la cantidad de notas: "))

while notes_counter <= notes:
    note_a = (float(input(f" Ingrese la nota numero {notes_counter}: ")))

    if note_a < 70:
        failed_grades += 1
        notes_f_t += note_a
 
    else:
        approved_grades += 1
        notes_a_t += note_a

    notes_t += note_a
    notes_counter += 1

average_approved = notes_a_t / approved_grades if approved_grades > 0 else 0
average_failed = notes_f_t / failed_grades if failed_grades > 0 else 0
average_grades_t = notes_t / notes if notes > 0 else 0

 
print(f" El estudiante esta cantidad de notas aprovadas: {approved_grades}")
print(f" El promedio de notas aprobadas: {average_approved:2f}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_grades}")
print(f"Este es el promedio de notas desaprobadas: {average_failed:.2f}")
print(f"Este es el promedio total de notas: {average_grades_t:.2f}")




        

        