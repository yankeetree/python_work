filename='pi_digit.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string+=line.rstrip()
print(pi_string[:52]+"....")
print(len(pi_string))