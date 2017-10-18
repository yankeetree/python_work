def count_words(words):
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		msg = 'sorry,the file '+filename+'does not exist.'
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("the file "+filename+" has about "+str(num_words)+" words.")

filename='alice.txt'
count_words(filename)



