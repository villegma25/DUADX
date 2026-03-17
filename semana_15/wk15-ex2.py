def bubble_sort_right_to_left(list_to_sort):
    outer_index = 0
    while outer_index < len(list_to_sort) - 1:
        has_made_changes = False
        index = len(list_to_sort) - 1 - outer_index

        # Move right → left
        while index > 0:
            current_element = list_to_sort[index]
            prev_element = list_to_sort[index - 1]

            if current_element < prev_element:  # smallest moves left
                list_to_sort[index], list_to_sort[index - 1] = prev_element, current_element
                has_made_changes = True
            index -= 1

        if not has_made_changes:
            break

        outer_index += 1


my_test_list = [1, 2, 3, 7, 4, 6, 8, 5, 10, 9]
bubble_sort(my_test_list)


print(my_test_list)