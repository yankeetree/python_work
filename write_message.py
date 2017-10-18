

while True:
	username=input('hello,please input your name:')
	print("welcome!")
	filename = 'programming.txt'

	with open(filename,'a') as file_object:
		file_object.write(username+"\n")
	