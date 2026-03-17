def ask_for_num():
    while True:
        try:
            num = float(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid value...")

def reset():
    return 0

def calcu(total):

    total = ask_for_num()

    while True:

        print("""
Select an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Reset total
6. Exit
""")
        op_num = input("Select an operation: ")

        if op_num == "1":
            second_value = ask_for_num()
            total = total + second_value
            print(f"Current total: {total}")

        elif op_num == "2":
            second_value = ask_for_num()
            total = total - second_value
            print(f"Current total: {total}")
        
        elif op_num == "3":
            second_value = ask_for_num()
            total = total * second_value
            print(f"Current total: {total}")
        
        elif op_num == "4":
            second_value = ask_for_num()
            if second_value == 0:
                print("Error: Cannot divide by zero.")
                continue
            total = total / second_value
            print(f"Current total: {total}")

        elif op_num == "5":
            total = reset()
            print(f"Total reset to: {total}")

        elif op_num == "6":
            break

        else:
            print("Invalid selection of operation...")

def main():
    total = 0
    print(f"Current total: {total}")
    calcu(total)

main()
