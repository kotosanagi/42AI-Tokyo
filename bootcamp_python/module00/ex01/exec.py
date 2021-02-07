import sys

args = sys.argv
sentence = ""

i = 1

for i in range(1, len(args)):
    sentence += args[i]

s = sentence.swapcase()[::-1]

print(s)
