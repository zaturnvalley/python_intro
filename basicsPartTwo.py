#function parameters
def addition(num1,num2,num3,num4):
  answer = num1 + num2 + num3 + num4
  return answer

x = addition(1,2,3,4)
print(x)

def website(font, background_color, font_size, font_color):
  print('font:', font)
  print('bg:', background_color)
  print('font Size:', font_size)
  print('font color:', font_color)

website('Futura','White','11','Black')
#can do out of order
website(font_color='black',
        font='TNR',
        font_size='11',
        background_color='black')
