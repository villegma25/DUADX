import math


num_prim = [1, 4, 6, 7, 13, 9, 67]
nums_filter = []



def split_first(text):
    return text.split(",") 


def is_prime(num):    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:            
            return False
            
            
    return True       
    

def list_prim(num):
    for num in num_prim:
      if is_prime(num):
        nums_filter.append(num)


def main():
    list_prim(num_prim)
    print(nums_filter)
    

main()
        




