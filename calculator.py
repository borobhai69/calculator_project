#import definitions
from math import *
from sympy import *
from py_expression_eval import Parser
#print("The program is running")
print("Welcome to the Python Derivative Calculator\n\n")
run = True
while run:
    print("To Begin, Enter an expression (include all operators): ")
    expression = input()
    parser = Parser()
    expr = parser.parse(expression)
    my_symbols = {}
    optionslist = ""
    counter = 0
    for var in expr.variables():
        my_symbols[var] = Symbol(var, real=True)
        if (counter == len(expr.variables()) - 1):
            optionslist += var
        else:
            optionslist += var + ", "
        counter+=1
    real_func = sympify(expr.toString(), my_symbols)
    dvar = input("What variable would you like to differentiate by?\n" + "Options: " + optionslist + '\n')
    if (dvar in my_symbols):
        diffated = diff(real_func, my_symbols[dvar])
    else:
        dvar = input("That isn't an option. Enter a new one.\n" + "Options: " + optionslist + '\n')
    print("The derivative is: " + str(diffated))
    print("What value would you like to plug in for the differentiated variable?")
    value = int(input())
    print("Your answer is: " + str(diffated.subs(my_symbols[dvar], value)))
    print("Would you like to try another function? (Y/N): ")
    rbool = input()
    if rbool.upper() == N:
        run = False