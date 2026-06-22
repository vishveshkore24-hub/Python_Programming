# write a program to display Data Type, Memory address, size in bytes

import sys
print("Variable Information")

variable = type(input("Please enter the variable")).__name__

if type(variable).__name__ == "int":
    variable = int(input("enter Inteer value : "))
elif type(variable).__name__ == "float":
    variable = float(input("enter the value"))
elif type(variable).__name__== "list":
    variable = list(input("Enter the list"))
else:
    print("Invalid data type")

print("Type of the variable : ", type(variable).__name__)
print("Memory address of variable : ", id(variable))
print("Size of variable , ", sys.getsizeof(variable))