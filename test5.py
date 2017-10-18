'''
alien_color=['green','yellow','red']
if alien_color=='green':
	print("the game player get 5 point.")
else:
	print("nothing")
'''
'''
requested_toppings=['mushtooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping=='green peppers':
		print("Sorry,we are out of green peppers right now.")
	else:
		print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")
'''
'''
names=['admin','john','tom','jake','lucy']
for name in names:
	if name=='admin':
		print("Hello "+name.title()+",woule you like to see a status report")
	else:
		print("hello")
'''
current_users=['zhao','qian','sun','li','zhou']
new_users=['wu','zheng','wang','sun','qian']
for new_user in new_users:
	for current_user in current_users:
		if new_user==current_user:
			print(new_user)
		else:
			print("nothing")
