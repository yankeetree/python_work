names="nick"
print("hello "+names+",would you like to learn some Python today?")

names1="wang"
print(names1.lower())
print(names1.upper())
print(names1.title())

name2="albert einstein"
message1=' A person who never made a mistake never tried anything new."'
print("\""+name2.title()+message1)

print(5+3)
print(2*4)
print(16/2)
print(10-2)

bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])

names=['wang','zhang','li']
print(names)
print(names[1])
##del names[1]
names[1]='zhao'
print(names)

names.insert(1,'shen')
print(names)
names.pop()
print(names)

names.sort()
print(names)

print(sorted(names,reverse=True))
print(names)
