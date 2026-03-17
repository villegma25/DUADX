def bubble_sort(list_to_sort):
    outer_index = 0
    while outer_index < len(list_to_sort) - 1:
        has_made_changes = False 
        index = 0

        while index < len(list_to_sort)-1 - outer_index:
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            print(f' inter {outer_index}, {index}. Current: {current_element}')

            if current_element > next_element:
                print('Current element is higher than the next one. Swaping...')
                list_to_sort[index], list_to_sort[index + 1 ] = next_element, current_element
                has_made_changes  = True
            index += 1

        if not has_made_changes:
            break

        outer_index += 1


my_test_list = [1, 2, 3, 7, 4, 6, 8, 5, 10, 9]
bubble_sort(my_test_list)


print(my_test_list)
