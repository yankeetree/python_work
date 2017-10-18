import pygal
from die import Die

die = Die()
die_1=Die()


results=[die.roll()*die_1.roll() for roll_num in range(1000)]

'''
for roll_num in range(1000):
	result=die.roll()+die_1.roll()
	results.append(result)
'''


frequencies=[]
max_result=die.num_sides*die_1.num_sides

frequencies=[results.count(value) for value in range(1,max_result+1)  ]
'''
for value in range(2,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)
'''
hist=pygal.Bar()

hist.title="result of rolling one D6"
hist.x_labels=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
hist.x_title="result"
hist.y_title="frequency"
hist.add('D6',frequencies)
hist.render_to_file('dice_visual.svg')

print(results)
print(frequencies)
