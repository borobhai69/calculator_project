# import definitions
from math import *
from sympy import *
from py_expression_eval import Parser
# print("The program is running")
print("Welcome to the Python Derivative/Integral Calculator\n\n")
run = True
while run:
    extra = ""
    nonselected = True
    while nonselected:
        print("Would you like to derive or integrate a function?\n(der, int): ")
        selection = input()
        if selection == "der":
            selection = "derive"
            nonselected = False
        elif selection == "int":
            selection = "integrate"
            extra = ", don't include dx in integrals"
            nonselected = False
        else:
            print("The calculator only works with the shown options")
    print("To Begin, Enter the expression you'd like to {} (include all operators{}):".format(
        selection, extra))
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
        counter += 1
    real_func = sympify(expr.toString(), my_symbols)
    if selection == "derive":
        dvar = input("What variable would you like to differentiate by?\n" +
                     "Options: " + optionslist + '\n')
        nonselected = True
        while nonselected:
            if (dvar in my_symbols):
                diffated = diff(real_func, my_symbols[dvar])
                nonselected = False
            else:
                dvar = input(
                    "That isn't an option. Enter a new one.\n" + "Options: " + optionslist + '\n')
        print("The derivative is: " + str(diffated))
        print("What value would you like to plug in for the differentiated variable?")
        value = int(input())
        print("Your answer is: " + str(diffated.subs(my_symbols[dvar], value)))
    else:
        dvar = input("What variable would you like to antidifferentiate by?\n" +
                     "Options: " + optionslist + '\n')
        nonselected = True
        while nonselected:
            if (dvar in my_symbols):
                nonselected = False
            else:
                dvar = input(
                    "That isn't an option. Enter a new one.\n" + "Options: " + optionslist + '\n')
        nonselected = True
        while nonselected:
            isDef = input(
                "Would you like the definite or indefinite integral? (def, ind): \n")
            if isDef == "def" or isDef == "ind":
                nonselected = False
            else:
                "Please enter one of the shown options"
        antidiffated = integrate(real_func, my_symbols[dvar])
        if isDef == "ind":
            print("Your solution is {}".format(str(antidiffated)))
        else:
            print("This is your integral in simplified indefinite form: {}".format(str(antidiffated)))
            endpoints = input(
                "Enter a and b vals for your definite integral as shown -> a, b:\n")
            rendpoints = endpoints.split(",")
            a = float(rendpoints[0])
            b = float(rendpoints[1])
            ans = integrate(real_func, (my_symbols[dvar], a, b))
            print("Your answer is {}".format(str(ans)))
    print("Would you like to try another function? (Y/N): ")
    rbool=input()
    if rbool.upper() == 'N':
        run=False