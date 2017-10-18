'''
message=input("Tell me something,and I will repeat it back to you:")
print(message)
'''
'''
prompt="please enter you age:"
prices=[10,15,3]
while True:
	a=input(prompt)
	if int(a)>=3 and int(a)<=10:
		print(prices[0])
	elif int(a)<3:
		print("free")
	else:
		print(prices[1])
'''
'''
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

#
while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	print("verifying user:"+current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

for user in unconfirmed_users:
	print(user)

'''
'''
pets=['cat','dog','cat','rabbit','cat','goldfish','bird']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)
'''
'''
responses={}
polling_active=True
while polling_active:
	name =input("\nWhat is your name?")
	response=input("Which mountain would you like to climb someday?")
	responses[name]=response
	repeat=input("would you like to let another person respond?(yes/no)")
	if repeat=='no':
		polling_active=False
print("\n---Poll Results---")
for name,response in responses.items():
	print(name+" would like to climb "+response+".")
'''
'''
sanwich_orders=['san1','san2','san3']
finished_sanwich=[]
while sanwich_orders:
	sanwich=sanwich_orders.pop()
	print("I made your tuna sandwich")
	finished_sanwich.append(sanwich)

for finish_sanwich in finished_sanwich:
	print(finish_sanwich)
'''
'''
sandwich_orders=['1','2','3','pastrami','pastrami','pastrami','4','5']
finished_sandwich=[]
print("pastrami sold out.")

while 'pastrami'in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(sandwich_orders)
'''


'''
	else:
		sandwich=sandwich_orders.pop()
		finished_sandwich.append(sandwich)
'''
'''
for finish_sandwich in finished_sandwich:
	print(finished_sandwich)
'''
'''
place=[]
active=True
while active:
	  
	prompt=input("which place would you like?:")
	place.append(prompt)
	repeat=input("continue?:")
	if repeat=='no':
		active=False
print(place)
'''
'''
def greet_user(username):
	print("hello "+username)
greet_user('jessi')
'''
'''
def display_message(title):
	print("have been study "+title)
display_message("jane'slove")
'''
'''
def describe_pet(pet_name,animal_type='dog'):
	print("\nI have a "+animal_type)
	print("My "+animal_type+"'s name is "+pet_name)
describe_pet('harry')
'''
'''
def make_shirt(shirt_size,shirt_font):
	print("the shirt size is:"+shirt_size)
	print("the shirt font is:"+shirt_font)

'''
'''
def get_formatted_name(first_name,last_name):
	full_name=first_name+last_name
	return full_name
while True:
	print("\nPlease tell me your name:")
	print("enter'q' at any time to quit")
	f_name=input("First name:")
	if f_name=='q':
		break
	l_name=input("Last name:")
	if l_name=='q':
		break
	musician=get_formatted_name(f_name,l_name)
	print(musician)
'''
'''
def build_person(first_name,last_name,age=''):
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
musician=build_person('jimi','hendrix',age=27)
print(musician)
'''
'''
def city_country(city_name,country_name):
	full_name=city_name+' '+country_name
	return full_name

while True:
	c_name=input("city name is:")
	if c_name=='q':
		break
	cou_name=input("country name is:")
	if cou_name=='q':
		break
	name=city_country(c_name,cou_name)
	print(name)
'''
'''
#8-7
def make_album(singer_name,album_name,singnumber=''):
	full_name={'singer':singer_name,'album':album_name}
	if singnumber:
		full_name['singnumber']=singnumber
	return full_name
while True:
	s_name=input("the album singer name is:")
	if s_name=='q':
		break
	a_name=input("the album name is")
	number=input("sings number is:")
	album=make_album(s_name,a_name,number)
	print(album)
'''
'''
def greet_users(names):
	for name in names:
		msg="hello "+name+"!"
		print(msg)
username=['hannah','ty','margot']
greet_users(username)
'''

