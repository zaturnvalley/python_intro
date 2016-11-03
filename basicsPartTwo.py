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
writeMe = 'example text'

saveFile = open('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()

##appending to a file