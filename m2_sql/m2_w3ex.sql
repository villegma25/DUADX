# SQL Normalization Exercises

=========================================================
EXERCISE 1 - EMPLOYEES AND PROJECTS
=========================================================

## Original Table (UNF)

| Employee ID | Employee Name | Department | Department Phone | Project ID | Project Name | Project Budget |
|-------------|---------------|------------|------------------|------------|--------------|----------------|
|201|Ana Rivera|IT|2222-2222|P001|Web App|50000|
|201|Ana Rivera|IT|2222-2222|P002|API REST|25000|
|202|Luis Mendez|Marketing|1111-1111|P003|Campaña TV|30000|

---------------------------------------------------------
FIRST NORMAL FORM (1NF)
---------------------------------------------------------

Primary Key: (EmployeeID, ProjectID)

All values are atomic and there are no repeating groups.

Problems:
- Employee information is repeated.
- Department information is repeated.
- Project information is repeated.

---------------------------------------------------------
SECOND NORMAL FORM (2NF)
---------------------------------------------------------

Employees

| EmployeeID | EmployeeName | Department | DepartmentPhone |
|------------|--------------|------------|-----------------|
|201|Ana Rivera|IT|2222-2222|
|202|Luis Mendez|Marketing|1111-1111|

Projects

| ProjectID | ProjectName | ProjectBudget |
|-----------|-------------|---------------|
|P001|Web App|50000|
|P002|API REST|25000|
|P003|Campaña TV|30000|

EmployeeProjects

| EmployeeID | ProjectID |
|------------|-----------|
|201|P001|
|201|P002|
|202|P003|

---------------------------------------------------------
THIRD NORMAL FORM (3NF)
---------------------------------------------------------

Departments

| DepartmentID | Department | DepartmentPhone |
|--------------|------------|-----------------|
|1|IT|2222-2222|
|2|Marketing|1111-1111|

Employees

| EmployeeID | EmployeeName | DepartmentID |
|------------|--------------|--------------|
|201|Ana Rivera|1|
|202|Luis Mendez|2|

Projects

| ProjectID | ProjectName | ProjectBudget |
|-----------|-------------|---------------|
|P001|Web App|50000|
|P002|API REST|25000|
|P003|Campaña TV|30000|

EmployeeProjects

| EmployeeID | ProjectID |
|------------|-----------|
|201|P001|
|201|P002|
|202|P003|

Justification

1NF
- Removed repeating groups.
- All values are atomic.

2NF
- Employee and project information depend on their own keys.
- Removed partial dependencies.

3NF
- Department information moved to its own table.
- Every non-key attribute depends only on the primary key.
- Eliminates redundancy and update anomalies.

=========================================================
EXERCISE 2 - STUDENTS AND COURSES
=========================================================

## Original Table (UNF)

| Student ID | Student Name | Course Code | Course Name | Instructor Name | Instructor Email |
|------------|--------------|-------------|-------------|-----------------|------------------|
|301|Marco Gómez|CS101|Python I|Juan Pérez|juan@uni.edu|
|301|Marco Gómez|CS102|Python II|Laura Rojas|laura@uni.edu|
|302|Carla Ruiz|CS101|Python I|Juan Pérez|juan@uni.edu|

---------------------------------------------------------
FIRST NORMAL FORM (1NF)
---------------------------------------------------------

Primary Key: (StudentID, CourseCode)

All values are atomic.

---------------------------------------------------------
SECOND NORMAL FORM (2NF)
---------------------------------------------------------

Students

| StudentID | StudentName |
|-----------|-------------|
|301|Marco Gómez|
|302|Carla Ruiz|

Courses

| CourseCode | CourseName | InstructorName | InstructorEmail |
|------------|------------|----------------|-----------------|
|CS101|Python I|Juan Pérez|juan@uni.edu|
|CS102|Python II|Laura Rojas|laura@uni.edu|

Enrollments

| StudentID | CourseCode |
|-----------|------------|
|301|CS101|
|301|CS102|
|302|CS101|

---------------------------------------------------------
THIRD NORMAL FORM (3NF)
---------------------------------------------------------

Students

| StudentID | StudentName |
|-----------|-------------|
|301|Marco Gómez|
|302|Carla Ruiz|

Instructors

| InstructorID | InstructorName | InstructorEmail |
|--------------|----------------|-----------------|
|1|Juan Pérez|juan@uni.edu|
|2|Laura Rojas|laura@uni.edu|

Courses

| CourseCode | CourseName | InstructorID |
|------------|------------|--------------|
|CS101|Python I|1|
|CS102|Python II|2|

Enrollments

| StudentID | CourseCode |
|-----------|------------|
|301|CS101|
|301|CS102|
|302|CS101|

Justification

1NF
- Atomic values only.

2NF
- Student information separated from course information.

3NF
- Instructor information separated from courses.
- No transitive dependencies remain.

=========================================================
EXERCISE 3 - HOSPITAL APPOINTMENTS
=========================================================

## Original Table (UNF)

| Appointment ID | Patient Name | Patient Phone | Doctor Name | Specialty | Date | Time |
|----------------|--------------|---------------|-------------|-----------|------------|----------|
|A01|Diana Vargas|8888-1111|Dr. Soto|Pediatría|2024-08-01|10:00 AM|
|A02|Diana Vargas|8888-1111|Dr. Soto|Pediatría|2024-08-10|10:00 AM|
|A03|Edwin Mora|8999-2222|Dr. Mora|Cardiología|2024-08-05|01:00 PM|

---------------------------------------------------------
FIRST NORMAL FORM (1NF)
---------------------------------------------------------

Primary Key: AppointmentID

All values are atomic.

Problems:
- Patient information is repeated.
- Doctor information is repeated.
- Specialty is repeated.

---------------------------------------------------------
SECOND NORMAL FORM (2NF)
---------------------------------------------------------

Patients

| PatientID | PatientName | PatientPhone |
|-----------|-------------|--------------|
|1|Diana Vargas|8888-1111|
|2|Edwin Mora|8999-2222|

Doctors

| DoctorID | DoctorName | Specialty |
|----------|------------|-----------|
|1|Dr. Soto|Pediatría|
|2|Dr. Mora|Cardiología|

Appointments

| AppointmentID | PatientID | DoctorID | Date | Time |
|---------------|-----------|----------|------------|----------|
|A01|1|1|2024-08-01|10:00 AM|
|A02|1|1|2024-08-10|10:00 AM|
|A03|2|2|2024-08-05|01:00 PM|

---------------------------------------------------------
THIRD NORMAL FORM (3NF)
---------------------------------------------------------

Specialties

| SpecialtyID | Specialty |
|-------------|-----------|
|1|Pediatría|
|2|Cardiología|

Doctors

| DoctorID | DoctorName | SpecialtyID |
|----------|------------|-------------|
|1|Dr. Soto|1|
|2|Dr. Mora|2|

Patients

| PatientID | PatientName | PatientPhone |
|-----------|-------------|--------------|
|1|Diana Vargas|8888-1111|
|2|Edwin Mora|8999-2222|

Appointments

| AppointmentID | PatientID | DoctorID | Date | Time |
|---------------|-----------|----------|------------|----------|
|A01|1|1|2024-08-01|10:00 AM|
|A02|1|1|2024-08-10|10:00 AM|
|A03|2|2|2024-08-05|01:00 PM|

Justification

1NF
- All values are atomic.
- No repeating groups.

2NF
- Patient and doctor information were separated from appointments.

3NF
- Specialty was moved to its own table.
- Every non-key attribute depends only on the primary key.
- Redundancy and update anomalies are eliminated.