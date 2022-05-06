import time
def marbles(): 
    marbles = int(input('How many marbles do you have: '))
    if marbles < 6:
        print('I have more marbles than you!')
    else:
        print('That is a lot of marbles')

def isthatyourname():
    name = input('Is your name john: ')
    if name == 'yes':
        print('That is my name too!')
    else:
        print('That is not a great name but it will do.')

def multinamecheck():
    name = input('What is your name: ')
    correctnames = ['John','George','Ringo','Paul']
    if name in correctnames:
        print('Hey that is the name of a Beatle!')
    else:
        print('That is a nice name')

def howinteresting():
    goals = int(input('How many goals were scored: '))
    if goals == 0:
        print('That game was boring')
    if goals < 3:
        print('That game was not the most interesting')
    if goals > 3 and goals < 6:
        print('That was a very interesting game')
    if goals > 6:
        print('That was unmissable')

def keepasking():
    footballteam = ''
    while footballteam != 'Cardiff':
        footballteam = input('What is your favorite football team: ')
    print('That is the correct answer')

def infiniteLoop():
    while 1:
        footballteam = input('What is your favorite football team: ')

def divideByCount():
    count = 5
    number = 0
    print("this programme will work out the total of a list of numbers") 
    while count > 0:
        number = number/int(input("Please enter a number :"))
        count -= 1 
        print(number)

def counter():
    for i in range(1,11):
        print(i)
        time.sleep(1)

def triangle():
    base = int(input('What is the length of the base of your triangle: '))
    height = int(input('How tall is the triangle: '))
    print('The area is: ' + str((base*height)/2))
triangle()