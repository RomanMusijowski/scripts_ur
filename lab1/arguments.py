import sys

args = len(sys.argv)

counter = 0
sentence = ""
for x in reversed(range(1, args)):
    if(len(sys.argv[x]) >= 3):
        counter += 1
        sentence += sys.argv[x]
        sentence += ' '

print(counter)
print(sentence)
