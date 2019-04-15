searchquery = 'am'

with open('Test.txt') as f1:
    with open('Output.txt', 'a') as f2:
        lines = f1.readlines()
        for i, line in enumerate(lines):
            if line.startswith(searchquery):
                f2.write(line)
                f2.write(lines[i + 1])
                f2.write(lines[i + 2])
