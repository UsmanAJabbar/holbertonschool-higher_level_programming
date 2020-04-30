#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
from sys import argv

# Import Guard
if __name__ == '__main__':
    # Get the argument count
    argc = (len(argv) - 1)
    operators = ['+', '-', '*', '/']
    functions = [add, sub, mul, div]

    # Check if argc is 3
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # If the argc == 3, asign the values
    a = int(argv[1])
    b = int(argv[3])

    # Search for the operator
    for symbols in range(len(operators)):
        # If argv[2] found an operator, call the func
        if argv[2] == operators[symbols]:
            # Save the return of the function
            # Save the operator found for print to use
            calc = functions[symbols](a, b)
            sign = operators[symbols]
            break
    # After looping through all the indexes
    # If the operator wasn't found, print error
    if argv[2] != operators[symbols]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # Else, Print the output
    print("{:d} {} {:d} = {:d}".format(a, sign, b, calc))
    exit(0)
