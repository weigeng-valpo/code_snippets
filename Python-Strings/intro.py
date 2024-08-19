message = 'Hello, World!'
print(message[10]) 
print(message[0:5]) 
print(message[6:]) 
# this is called slicing

print(message[-1]) 
print(message[-5:-2]) 
# doing backward slicing

print(len(message))

greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {name}'
print(message)

print(help(str.lower))
print(help(str.upper)) 