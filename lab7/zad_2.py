def count_2sub_match(a, b):
	sum = 0
	temp = [b[i:i + 2] for i in range(0, len(b), 2)]
	print(temp)
	output = set()
	for x in temp:
		output.add(x)
	print(output)
	for letters in output:
		sum = sum + a.count(letters)
	return sum
	
print(str(count_2sub_match('abcdz', 'ababdz')))
print(str(count_2sub_match('abcdab', 'ab')))