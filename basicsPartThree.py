# making modules
import exampleModule

exampleModule.exampleFunc('test')

#pre built in modules are in python lib
#third part modules are in packages
#needs to be in local dir of proj yr working on in lib

#error handling with try and accept
try:
  print('Running the try...')
  import mars #this will throw import error
  print('5'+5)

  #will say type error cannot print int to string
except Exception as e:
  print('General Exception')
  pring(str(e))

except TypeError as t:
  print('TypeError Triggered')
  pring(str(t))

except NameError as n:
  print('NameError Triggered')
  pring(str(n))

print('Code continues onward...')

# try:
#   name = input('what is your name')
#   print(str(name))

