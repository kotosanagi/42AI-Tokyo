import sys

args = sys.argv
n_len = len(args)

def sum_func(num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    return n1 + n2

def dif_func(num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1

def mlt_func(num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    return n1 * n2

def div_func(num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    if n2 == 0:
        return "ERROR (div by zero)"
    else:
        return n1 / n2

def mod_func(num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    if n2 == 0:
        return "ERROR (modulo by zero)"
    else:
        return n1 % n2

def exit_error():
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit()

if n_len > 3:
    print("InputError: too many arguments")
    exit_error()
elif n_len == 2:
    print("InputError: too few arguments")
    exit_error()
elif n_len == 1:
    exit_error()
elif not(args[1].isdigit()) or not(args[2].isdigit()):
    print("InputError: only numbers")
    exit_error()

print("Sum:         " + str(sum_func(args[1], args[2])))
print("Difference:  " + str(dif_func(args[1], args[2])))
print("Product:     " + str(mlt_func(args[1], args[2])))
print("Quotient:    " + str(div_func(args[1], args[2])))
print("Remainder:   " + str(mod_func(args[1], args[2])))

