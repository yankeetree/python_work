
def city_country(city,country,population=''):
	if population:
		fullname=city+','+country+'-population='+str(population)
	else:
		fullname=city+','+country
	
	return fullname.title()
