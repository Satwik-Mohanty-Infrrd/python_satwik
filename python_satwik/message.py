message= 'Hello World'

print(message)
print(message[0])
print(message[10])
print(message[0:5])
print(message[6:])
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))

new_message= message.replace('World', 'Universe')
print(new_message)

greeting= 'Hello'
name= 'Satwik'

m= greeting+','+name 
print(m)

me= '{}, {}. Welcome!'.format(greeting, name)
print(me)

fme= f'{greeting}, {name}. Welcome!'
print(fme)


print(dir(name))
print(help(str.lower))