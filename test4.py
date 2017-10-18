'''
animals=['cat','dot','pet']
for animal in animals:
	print(animal)
	
for animal in animals:
	print("A "+animal.title()+" make a great pet.")
print("Any of these animals would make a great pet!")

for value in range(1,5):
	print(value)

even_number=list(range(2,11,2))
print(even_number)


squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)

for value in range(1,21):
	print(value)

squeares1=list(range(1,1000001))
for value in squeares1:
	print(value)


squares2=list(range(1,1000001))
print(min(squares2))
print(max(squares2))
print(sum(squares2))

squares3=list(range(1,21,2))
for value in squares3:
	print(value)
'''

players=['tom','book','good','well']
for player in players[0:2]:
	print(player)
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print(my_foods)
print(friend_foods)

dimensions=(200,50)
print(dimensions[0])


cars=['audi','bmw','subru','toyota']
for car in cars:
	if car=="bmw":
		print(car.upper())
	else:
		print(car.title())
		



