'''
alien_0={'color':'green','point':5}
print(alien_0['color'])
print(alien_0['point'])
'''
'''
user_0={
'username':'efermi',
'first':'enrico',
'last':'fermi'}

for key,value in user_0.items():
	print("\nkey: "+key)
	print("value: "+value)
'''

'''
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}
friends=['phil','sarah']
for name in favorite_languages:
	print(name.title())
	
	if name in friends:
		print(" Hi "+name.title()+favorite_languages[name].title()+"!")
'''
'''
rivers={'yangzi':'China','nile':'egypt','huanghe':'China'}
for river,nation in rivers.items():
	print("The "+river+" runs through "+nation)
	
for river in rivers.keys():
	print(river)
	
for nation in rivers.values():
	print(nation)
'''
'''
alien_0={'color':'green','point':5}
alien_1={'color':'yellow','point':10}
alien_2={'color':'red','point':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
'''
'''
aliens=[]

for alien_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
	
for alien in aliens[:5]:
	print(alien)
print("...")

print("Total numbeer of aliens:"+str(len(aliens)))
'''
'''
pizza={
	'crust':'thick','toppings':['mushroom','extra cheese']

}
print("you ordered a "+pizza['crust']+"-crust pizza "+"with the following toppings:")
for topping in pizza['toppings']:
	print("\t"+topping)
'''
'''
favorate_languages={
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell']
}
for name,languages in favorate_languages.items():
	if len(languages)==1:
		print("\n"+name.title()+"'s favorate languages is:")
	else:
		print("\n"+name.title()+"'s favorate languages are:")
	for language in languages:
			print("\t"+language.title())
'''

users={
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton'
		},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris'
		}
	
}
for username,user_info in users.items():
	print("\nUsername:"+username)
	full_name = user_info['first']+" "+user_info['last']
	location=user_info['location']
	
	print("\tFull_name: "+full_name.title())
	print("\tLocation:"+location.title())
