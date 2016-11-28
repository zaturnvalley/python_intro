# Python Notes
# # making modules
# import exampleModule

# exampleModule.exampleFunc('test')

#pre built in modules are in python lib
#third part modules are in packages
#needs to be in local dir of proj yr working on in lib

#error handling with try and accept
# try:
#   print('Running the try...')
#   import mars #this will throw import error
#   print('5'+5)

  #will say type error cannot print int to string
# except Exception as e:
#   print('General Exception')
#   pring(str(e))

# except TypeError as t:
#   print('TypeError Triggered')
#   pring(str(t))

# except NameError as n:
#   print('NameError Triggered')
#   pring(str(n))

# print('Code continues onward...')

# try:
#   name = input('what is your name')
#   print(str(name))

#lists vs tuples and list manipulation
# def example() :
#   return 15,19
# #tuple examples (immutable):  
# a,b = example()
# 3,4,5,6
# (53,56,4)
# print(a)
# print(b)

#list example (mutable, sim to array but not)
# xList = [5,4,3,2,2]

# print(xList)
# print(xList[2])

# # adds to list end
# xList.append(12)
# print(xList)
# # insert into spot
# xList.insert(4,300)
# print(xList)
# # will remove first seven
# xList.remove(5)
# print(xList.index(4))
# print(xList.count(2))
# xList.sort()
# print(xList)

# # changing value of xList
# xList = ['bill', 'ted', 'jan', 'donna']
# print(xList)

# # changes order / mutates list
# xList.sort()
# print(xList)
# # reverse list
# xList.reverse()
# print(xList)

# dictionaries (similar to object in JS, also mutable, key value paris)

gradeDict = {'John':90, 'David':65, 'Jack':95}
print(gradeDict)
print(gradeDict['David'])
#can update, mutable
gradeDict['David'] = 70
print(gradeDict)
gradeDict['John'] = 92