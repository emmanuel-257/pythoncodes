num_1 = input("Input first number: ")
num_1 = int(num_1)
num_2 = input("Input second number: ")
num_2 = int(num_2)
operation = input("Input operation (+, -, *, /): ")

# this is where we perform the operations according to the user input
if operation == '+':
    print(num_1 + num_2)
elif operation == '-':
    print(num_1 - num_2)
elif operation == '*':
    print(num_1 * num_2)
elif operation == '/':
    if num_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num_1 / num_2)
else:
    print("Invalid operation")

