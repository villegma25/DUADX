my_list =[4, 3, 6, 1, 7]
if len(my_list) > 1:
    first_element = my_list[0]
    last_element = my_list[len(my_list) - 1]

    temp = first_element
    my_list[len(my_list) - 1]= temp
print(my_list)
