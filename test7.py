'''
message=input("Tell me something,and I will repeat it back to you:")
print(message)
'''
'''
message=input("how many people?: ")
if int(message)>18:
	print("there's no ")
else:
	print("have")
'''
'''
prompt="\nTell me something,and I will repeat it back it to you: "
prompt+="\nEnter 'quit' to end the program."
active=True

while active:
	message=input(prompt)
	if message=='quit':
		active=False
	else:
		print(message)
'''

prompt="\nPlease enter the name of a city you have visited:"
prompt+="\n(Enter 'quit' when you are finished.)"

while True:
	city =input(prompt)
	if city =='quit':
		break
	else:
		print("I'd love to go to "+city.title()+"!")
