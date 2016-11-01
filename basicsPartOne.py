#python print and strings
print('hi')
print('good to meet','you')
print(5+4)
print('my favorite number is', 10)

#python math
print(2/3) #new to python 3 prints .33 
print(2*3)
print(1.5/2.6) #floats
print(4**2) #4 to the power of 2

#python variables
exVar = 100
print(exVar)
opVar = exVar / 5
print(opVar)
#cannot use numbers at beginning, so use underscore before, ie:
_100ma = 5
print(_100ma)

#seems super similar to ruby so far, except print instead of puts

#while loops
condition = 1
while condition <= 10: 
    print(condition)
    '''
    multi line comment with triple quote
    '''
    condition += 1

condition = 5

while condition > 0:
    print('true', condition)
    condition -= 1

#for loops
exampleList = [1,6,7,3,6,9,0]
for thing in exampleList:
    print(thing)
    
for x in range(1,11):
    print('range', x)

#if statements
a = 2
b = 7
c = 10

if c > b:
    print(c, 'is greater than', b)
if c == b + 3:
    print('both ten')

#if else
if c < b:
    print(c, 'is greater than', b)
else:
    print(b, 'is not greater than', c)
    
#elif
if c < b:
    print(c, 'is greater than', b)
elif c > b:
    print(b, 'is not greater than', c, 'using elif')
else:
    print('nope')

#functions
def example():
    print('example function')

example()

