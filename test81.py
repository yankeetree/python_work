'''
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

while unprinted_designs:
	current_design=unprinted_designs.pop()
	print("print model:"+current_design)
	completed_models.append(current_design)

print("\nthe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)
'''
'''
def print_models(unprinted_designs,completed_models):
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		print("printing models"+current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nthe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
'''
'''
def show_magicians(magicians_names):
	for magician_name in magicians_names:
		print(magician_name)

def make_great(un_list,com_list):	
	while un_list:
		cur_list2=un_list.pop()
		cur_list2='the great '+cur_list2
		com_list.append(cur_list2)

magician_names=['zhang long','zhaohu','wangzhao','mahan']
new_magician_names=[]
make_great(magician_names[:],new_magician_names)

show_magicians(new_magician_names)
show_magicians(magician_names)

'''
'''
def show_magicians(new_magicians):  #打印函数
    for magician in new_magicians:   #遍历列表
        print(magician.title())

def make_great(magicians,new_magicians):    #对列表修改的函数
    while magicians:
         current_magician = magicians.pop()    #删除原列表中的元素
         current_magician = "The Great " + current_magician
         new_magicians.append(current_magician)

magicians = ['tom','jack','marry']   #创建魔术师列表
new_magicians = []      #用于保存修改后的列表元素
make_great(magicians[:],new_magicians)  #传递列表副本
show_magicians(new_magicians)    #调用show_magician()函数
show_magicians(magicians)
'''

'''
def make_pizza(size,*toppings):
	print("\nMaking a "+str(size)+"-inch pizza with the following toppings:" )
	for topping in toppings:
		print("- "+topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushroms','green peppers','extra cheese')
'''
'''
def build_profile(first,last,**user_info):
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile

user_profile=build_profile('yan','qiang',location='beijing',field='chaoyang',age='16')
print(user_profile)
'''
'''
def food_sanwich(*food):
	print(food)

food_sanwich('peppy')
food_sanwich('rice','egg')
food_sanwich('juice','apple','orange')
'''
'''
def make_car(company,model,**car_info):
	prom={}
	prom['company_name']=company
	prom['model_name']=model
	for key,value in car_info.items():
		prom[key]=value
	return prom

car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
'''

def make_pizza(size,*toppings):
	print("\nMaking a "+str(size)+"-inch pizza with the following toppigns:")
	for topping in toppings:
		print("- "+topping)


