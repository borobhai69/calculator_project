import definitions
from math import *
import re
print("The program is running")

print("Welcome to the Python Integration and Differentiation Calculator\n\nTo begin, enter 'I' for integration and 'D' for differentiation")
answer = input()
print("Enter an expression without space (formats:\n\t\t\t\t\t\tnx^p+nx^p...\n\t\t\t\t\t\tnx^p-nx^p...): ")
expression = input()


# split expression into a list of strings
res = re.split('-|\+', str(expression))
# print(res)

# get derivative of single expression
def g(exp):
    if exp[0:2].isnumeric():
        mult = int(exp[0:2])*int(exp[4:])
        power = int(exp[4:])-1
    elif exp[0].isdigit():
        mult = int(exp[0])*int(exp[3:])
        power = int(exp[3:])-1
    else:
        mult = int(exp[2:])
        power = int(exp[2:])-1
    return str(mult) + "x" + "^" + str(power) + " "
# print(g(expression))

# get antiderivative of expression
def a(exp):
    if exp[0:2].isnumeric():
        p = int(exp[4:])+1
        check = int(exp[0:2])/p
        if check.is_integer():
            return str(check) + "x" + "^" + str(p) + " "
        else:
            return "(" + exp[0:2] + "x" + "^" + str(p) + ")" + "/" + str(p) + " "
    elif exp[0].isdigit():
        p = int(exp[3:])+1
        check = int(exp[0])/p
        if check.is_integer():
            return str(check) + "x" + "^" + str(p) + " "
        else:
            return "(" + exp[0] + "x" + "^" + str(p) + ")" + "/" + str(p) + " "
    else:
        p = int(exp[2:])+1
        return "x" + "^" + str(p) + "/" + str(p) + " "

# separate the operators in expression into a list
op = []
for n in range(len(expression)):
    if str(expression[n]) == "+" or str(expression[n]) == "-":
        op += str(expression[n])

# get the derivative of each res and add it to a string
deriv = ""
for i in res:
    if answer.upper() == "D":
        deriv += str(g(i))
    elif answer.upper() == "I":
        deriv += str(a(i))

# split that string into a list of derivatives
total = re.split(' ', deriv)
# remove the extra space at the end
total.remove('')
# print(total)

# finally, merge the list of operators and derivatives
merge = []
for z in range(len(op)):
    merge += total[z] + op[z]
# merge the final string in total
merge += total[len(total)-1]
# print(merge)

# convert the list into a string
def listToString(s):
    str1 = ""
    return (str1.join(s))
if answer.upper() == "D":
    print("The derivative is: " + listToString(merge))
elif answer.upper() == "I":
    print("The antiderivative is: " + listToString(merge))

# def f(n):
#     return int(expression[0])*n**int(expression[3:])
# value = int(input("Enter an x value of the derivative: "))
# print(derive(f, value))
#  def derive(function, value):
#     h = 0.00000000001
#     top = function(value + h) - function(value)
#     bottom = h
#     slope = top / bottom    # Returns the slope to the third decimal
#     return int(float("%.3f" % slope))
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.