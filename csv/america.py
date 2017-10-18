import pygal

wm=pygal.Worldmap()
wm.title='North,Central,and South America'

wm.add('North America',['ca','mx','us'])
wm.render_to_file('america.svg')