with open(input('Enter file name: '), 'r') as f:
    w = [len(word) for line in f for word in line.rstrip().split(" ")]
    w_avg = sum(w)/len(w)
