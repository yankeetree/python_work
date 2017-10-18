#9-1/9-4
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.name=restaurant_name
		self.type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print(self.name)
		print(self.type)
		print(self.number_served)

	def open_restaurant(self):
		print("the restaurant is open.")

	def set_number_served(self,number_served):
		self.number_served=number_served

	def increment_number_served(self,incre_number):
		self.number_served+=incre_number


class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['berry','bulin','orange']



restaurant=Restaurant('holiday','super')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(9)
restaurant.describe_restaurant()
restaurant.increment_number_served(20)
restaurant.describe_restaurant()
the_shop=IceCreamStand('holiday','super')
print(the_shop.flavors)