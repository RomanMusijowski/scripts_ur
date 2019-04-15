def is_build_pos(small, large, goal):
	LARGE = 5
	SMALL = 1
	length = 0
	ref_goal = goal
	
	for y in range(0, large):
		if(ref_goal > LARGE):
			length = length + LARGE
			ref_goal = ref_goal - length
		else:
			break
	for x in range(0, small):
		length = length + SMALL

	print(length, goal, ref_goal)
	if length == goal:
		return True
	else:
		return False
	
print(str(is_build_pos(3, 1, 8))) # True
print(str(is_build_pos(3, 2, 9))) # False