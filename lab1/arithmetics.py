import sys

a = int(sys.argv[1])
b = int(sys.argv[3])

if sys.argv[2] == "+":
    result = a+b
if sys.argv[2] == "-":
    result = a-b
if sys.argv[2] == "*":
    result = a*b

print(result)
