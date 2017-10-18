import json
inputnum=input("input your favourate number:")
filename='inputnum.json'
with open(filename,'w') as file_object:
	json.dump(inputnum,file_object)
	print("favorate num is:"+inputnum)


