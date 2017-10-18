


while True:
	a = input("input your first number:")
	if a=='q':
		break
	b = input("input your second number:")
	if b=='q':
		break
	try:
		c=int(a)+int(b)
	except ValueError:
		print("wrong")
	else:
		print(c)