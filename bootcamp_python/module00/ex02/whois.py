import sys

args = sys.argv
len_arg = len(args)

if len_arg != 2:
    print("ERROR")
    sys.exit(1)

if not (args[1].isnumeric()):
    print("ERROR")
    sys.exit(1)

num = int(args[1])

if num == 0:
    print("I'm Zero.")
elif num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
