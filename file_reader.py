filename = 'pi_digit.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
