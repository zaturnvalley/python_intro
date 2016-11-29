# Program For Keeping a Log of Student Grades

#imports
from statistics import mean as m

#constants
admins =  {'Python':'Pass123@', 'user2':'pass2'}

studentDict = {'Jack':[80,90,88],
               'Alex':[94,59,69],
               'Beth':[49,100,99]}
#methods to be called in program
def enterGrades():
  nameToEnter = input('Student Name: ')
  gradeToEnter = input('Grade: ')

  if nameToEnter in studentDict:
    print('Adding Grade...')
    studentDict[nameToEnter].append(float(gradeToEnter))
  else:
    print('Student does not exist.')
  print(studentDict) 

def removeStudent():
  nameToRemove = input('What student to remove?: ')
  if nameToRemove in studentDict:
    print('removing student...')
    del studentDict[nameToRemove]
    print(studentDict)
def studentAVGs():
  for eachStudent in studentDict:
    gradeList = studentDict[eachStudent]
    avgGrade = m(gradeList)

#program
def main():
  print("""
  Welcome to Grade Central

  [1] - Enter Grades
  [2] - Remove Student
  [3] - Student Average Grades
  [4] - Exit
  """)
  action = input('What would you like to do today? (Enter a number ')

  if action == '1':
    enterGrades()
  elif action = '2':
    removeStudent()
  elif action = '3':
    print('3')
  elif action == '4':
    exit()
  else:
    print('No valid choice was given, try againg')



login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
      print('Welcome,',login)
        while True:
          main()
    else:
      print('Invalid password')
else:
  print('Invalid username')