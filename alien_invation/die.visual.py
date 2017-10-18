import pygal
from die import Die

die = Die()
die_1=Die()

results=[]

for roll_num in range(1000):
	result=die.roll()+die_1.roll()
	results.append(result)

frequencies=[]
max_result=die.num_sides+die_1.num_sides

for value in range(2,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)

hist=pygal.Bar()

hist.title="result of rolling one D6"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="result"
hist.y_title="frequency"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')


print(frequencies)
