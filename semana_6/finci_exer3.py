num_list  = [4, 6, 2, 29]

def sum_list(num_list):
    sum_tot = 0

    for num in num_list:
        sum_tot += num

    return sum_tot

result = sum_list([4, 6, 2, 29])
print(result)