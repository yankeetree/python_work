filename='study_in_python.txt'

with open(filename) as file_object:
	contents=file_object.read()
	
	print(contents.replace('python','C').rstrip())

with open(filename) as file_object:
	lines=file_object.readlines()	
	for line in lines:


		
		print(line.replace('python','c').rstrip())
	    

with open(filename) as file_object:
	lines1 = file_object.readlines()

pi_string = ''
for line in lines1:
	pi_string+=line.rstrip()
print(pi_string)

