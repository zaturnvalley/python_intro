#function parameters
def addition(num1,num2,num3,num4):
  answer = num1 + num2 + num3 + num4
  return answer

x = addition(1,2,3,4)
print(x)

# def website(font, background_color, font_size, font_color):
#   print('font:', font)
#   print('bg:', background_color)
#   print('font Size:', font_size)
#   print('font color:', font_color)

# website('Futura','White','11','Black')
# #can do out of order
# website(font_color='black',
#         font='TNR',
#         font_size='11',
#         background_color='black')

#can customize defaults this way
def website(font='TNR', 
            background_color='black', 
            font_size=11, 
            font_color='white'):
  print('font:', font)
  print('bg:', background_color)
  print('font Size:', font_size)
  print('font color:', font_color)

#then can change those defaults via this
website(background_color = 'green')

#writing to a file
writeMe = 'example text created with write'
#w for write
saveFile = open('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()

##appending to a file

appendMe = 'some more text created with append'
#a for append
saveFile = open('exampleWrite.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

#reading from a file
readMe = open('exampleWrite.txt', 'r').read()
print(readMe)
#puts into python list
splitMe = readMe.split('\n')
print(splitMe[1])

#this will show new lines via \n
readMe2 = open('exampleWrite.txt','r').readlines()
print(readMe2)

#classes
class calc:

  def add(x,y):
    answer = x+y
    print(answer)
  def sub(x,y):
    answer = x-y
    print(answer)
  def mult(x,y):
    answer = x*y
    print(answer)
  def div(x,y):
    answer = x/y
    print(answer)

#Input and statistics
#Input from User:
"""
name = input('what is your name?: ')
print('Hello ', name)
"""
##import statistics 
##
##exList = [5,4,3,2,6,3]
##x = statistics.mean(exList)
##print(x)
##
##x = statistics.median(exList)
##print('median', x)
##
##x = statistics.mode(exList)
##print('mode', x)
##
##x = statistics.stdev(exList)
##print('stdev', x)
##
##x = statistics.variance(exList)
##print('variance', x)

#import syntax
from statistics import mean as m
##import statistics as s
myList - [3,4,7,8,3,1]
##print(s.mean(exList))
print('stat mean import syntx', m(myList))


