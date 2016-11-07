# making modules
import exampleModule

exampleModule.exampleFunc('test')

#pre built in modules are in python lib
#third part modules are in packages
#needs to be in local dir of proj yr working on in lib

#error handling
try:
  print('Running the try...')
  import mars #this will throw import error
  print('5'+5)

  #will say type error cannot print int to string
except Exception as e:
  pring(str(e))
  print('General Exception')

except TypeError as t:
  print('TypeError Triggered')

except NameError as n:
  print('NameError Triggered')

except Exception as e:

print('Code continues onward...')