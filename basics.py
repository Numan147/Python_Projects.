'''
def one():
    x=int(input("Enter your first no: "))
    y =int(input("Enter your second no: "))
    print("Sum of both no : ", x+y)
one()

def two():
    a = int(input("Enter your first no: "))
    b = int(input("Enter your second no: "))
    print("Product of both no : ", a*b)
two()

def three():
    a = int(input("Enter your first no: "))
    b = int(input("Enter your second no: "))
    print("Subtraction of both no : ", a-b)
three()


def four():
    a = int(input("Enter your first no: "))
    b = int(input("Enter your second no: "))
    print("Divison : ", a/b)

four()


def five():
    a = int(input("Enter your first no A : "))
    b = int(input("Enter your second no B : "))
    print("Reminder of A/B = ", a%b)
five()

def six():
    a = float(input("Enter your first no : "))
    b = float(input("Enter your second no : "))
    print("Sum of both no : ", a+b)
six()


def seven():
    a = float(input("Enter your first no : "))
    b = float(input("Enter your second no : "))
    print("Sum of both no : ", a * b)
seven()


def eight():
    a = float(input("Enter your first no : "))
    b = float(input("Enter your second no : "))
    print("Subtraction of both no : ", a - b)
eight()


def nine():
    a = float(input("Enter your first no : "))
    b = float(input("Enter your second no : "))
    print("Divison of both no : ", a/b)
nine()


def ten():
    a = float(input("Enter your first no A: "))
    b = float(input("Enter your second no B: "))
    print("Reminder of A/B : ",a%b)
ten()

#Write a C program that calculates total, average and percentage of 5 subjects of a student. Take inputs from user

def eleven():

    a = float(input("Enter your scored marks in Math subject : "))
    b = float(input("Enter your scored marks in English subject : "))
    c = float(input("Enter your scored marks in History subject : "))
    d = float(input("Enter your scored marks in Algebra subject : "))
    e = float(input("Enter your scored marks in Science subject : "))
    total = int(a+b+c+d+e)
    print("Sum of all Subject : ", total)
    avg= total/5
    print("Average of total marks obtained : ",avg)
    max_marks = 500
    x = (total/max_marks)*100
    print("Total Marks Percentage : ",x,"%")

eleven()

# Write a program to enter length and breadth of a rectangle and find
# its perimeter.
# Formula: P=2(l+w);
# Where l is length and w are the width of rectangl
def twelve():
    l = int(input("Enter length of side of Rectangle : "))
    b = int(input("Enter Breadth of side of Rectangle : "))
    p = int(l+b)*2
    print("Perimeter of Rectangle : ",p)

twelve()


# Write a program to find area of a rectangle
# Formula: area=l*b;
# Where l is length and w are width of the rectangle

def thirteen():
    l = int(input("Length of your side of rectangle : "))
    b = int(input("Breadth of your side of rectangle : "))
    area= print(l*b,"Is area of your rectangle")
thirteen()

# Write a program to find surface area of a cuboid
# Formula: S=2(l+w+h);
# Where l is length, w is width and h are the height of the cuboid

def fourteen():
    l = int(input("Please Length of cuboide : "))
    w = int(input("Please Width of cuboide : "))
    h = int(input("Please Height of cuboide : "))
    s=2*(l + w + l)
    print("Surface area of cuboide is",s)

fourteen()


# Write a program to find surface area of a cuboid
# Formula: S=2(l*w*h);
# Where l is length, w is width and h are the height of the cuboid.
def fifteen():
    l = int(input("Please Length of cuboide : "))
    w = int(input("Please Width of cuboide : "))
    h = int(input("Please Height of cuboide : "))
    s=2*(l*w + w*h + h*l)
    print("Surface area of cuboide is",s)

fifteen()

# Write a C program that accepts an employee's ID, total worked hours
# of a month and the amount he received per hour. Print the employee's
# ID and salary (with two decimal places) of a particular month

def sixteen():
    wages=float(15)
    print("Per hour working wage is 15 dollar for employees.")
    id = int(input("Enter your ID : "))
    workingHour=float(input("Enter your worked hours this month : "))
    hr=wages*workingHour
    #print(format('Employess No',id,'Salary for this Month',wages*workingHour,".2f"))
    print("Total pay given to employee no",id," ${:,.2f}".format(hr))
sixteen()
'''
'''
# 17.Write a C program to calculate a bike’s average consumption from
# the given total distance (integer value) travelled (in km) and spent fuel
# (in litters, float number – 2 decimal point).

def seventeen():
    fuel=12.35
    td = int(462)
    #print("Distance travelled",td,"Kms")
    a = td/fuel
    print("Bike is giving avg for per ltr fuel {:,.2f}".format(a))
seventeen()
'''
'''
# .Write a C program to calculate the distance between the two points.
def eighteen():
    pointOne=16
    pointTwo=10
    distance=(pointOne-pointTwo)
    print("Distance between point one and point two is",distance)
eighteen()

'''
'''
# Write a C program to read an amount (integer value) and break the
# amount into smallest possible number of bank notes.

def nineteen():
    def count(amount):
        notes=[2000,1000,500,200,100,50,20,10,5,2,1]
        notesCount={}
        for note in notes:
            if amount >= note:
                notesCount[note]=amount//note
                amount= amount % note
        print("Currency count ->")
        for key, val in notesCount.items():
            print(key,":",val)
    amount=(15250)
    count(amount)

nineteen()
'''
'''
# .Write a C program to convert a given integer (in seconds) to hours,
# minutes and seconds
def twenty():
    givenSec=int(input("Enter a integer to convert in(seconds) to hours to minutes : "))
    print("Given no: ",givenSec)
    def secsToHMS(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 30
        seconds %= 60
        a = ('%d:%02d:%02d' % (hour,minutes, seconds,))
        print("Integer in (Seconds) successfully converted into HOURS,MINUTES,SECONDS format.\nBelow you can see the true format:-\nHours:Minutes:Seconds")
        print(a)
    n = givenSec
    return(secsToHMS(n))

twenty()
'''
'''
def twentyone():
    a=int(input("enter your number : "))
    b=int(input("enter your number : "))
    if a == b:
        print("Numbers equal")
    else:
        print("Numbers not equal")

twentyone()
'''

   






