list_of_keys = ['access_level', 'age']
employee = {
    'name': 'john',
    'email' : 'jhon@corp.com',
    ' access_level' : 5,
     'age' : 28
}

for key in list_of_keys:
    employee.pop(' access_level', 'age'   )

print(employee)    