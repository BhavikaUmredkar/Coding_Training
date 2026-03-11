# math = 40
# pi =3.14
# name = 'Bhavika Umredkar'
# print (type(math))
# print(type(pi))
# print(type(name))

# #type casting
# print(2+22)
# print("2"+"2")


# #input function by default string hota h
# #val1 = input("enter 1st value")
# #val2 = input("enter 1st value")
# #print(val1+val2)

# #al1 = int(input("enter 1st value"))
# #val2 = int(input("enter 1st value"))
# #print(val1+val2)

# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))
# #complex values cant be typecasted  cant convert comolex into int print(int(10+5j))
# #cant string into int   , convert float intointp

# print(float(3))
# print(float(True))
# print(float(False))
# print(float("4"))
# print(float(4.22))
# #print(float('hello'))
# #can't complex value to float  string to float

# print(complex(3))
# print(complex(True))
# print(complex(12.5))
# print(complex(True,False))
# #print(complex('hello'))
# # can't convert string to complex


# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+3j))
# print(bool(-1))
# print(bool('nishika'))#strig bhi true
# print(bool( )) # empty braket false
# print(bool(" " )) # empty string is true
# # 0 in any format we recive output 0 int float false complex = false baki true


#WAP for simple interest
# principal = 100000
# roi = 10
# time = 1
# si = principal*roi*time/100
# print("Simple Interest = ",si)


#C = float(input(("celsius:")))
#F = (C*9/5) + 32
#print("Farhenite:",F)

#val1=int(input("Enter 1st number:"))
#val2=int(input("Enter 2nd number:"))
#temp = val1
#val1 = val2
#val2 = temp
#print(val1,val2)

# a = 100
# b = 200
# a = a+b
# b = a-b
# a = a-b
# print(a,b)

# feet =float(input("Feet:"))
# inch = feet*12
# cm = inch*2.54
# print(inch)
# print(cm)

# num = 123
# print(num)
# a = num % 10
# num = num //10
# b = num % 10 #b=2
# c = num // 10
# rev = a*100 + b*10 + c*1 #300+20+1
# print(rev)

# mylist = ["Prashant","Ashish","Komal","ankush","77","sandip","60.75","prasant"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)

# mylist.insert(1,'sanket')
# print(mylist)

# mylist.remove('sandip')
# print(mylist)

# newlist = mylist.copy() # cloning
# print(mylist)
# print(newlist)

# mylist = [['Bhavika','Umredkar'],['85','56'],['440024','yyy']]
# print("example of multidimensional list:")
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1=['prshant','jha']
# print(list1*2)

# list2=[50,25,30,'prashant']
# del list2[2]
# print(list2)

# list2=[50,25,30,'prashant']
# list2.clear()
# print(list2)

# name="prahsnat"
# print(name)
# myname=list(name) #typecasting
# print(name)

#sorting expample
# mylist=[44,22,77,0,9,88]
# mylist.sort()
# print(mylist)

# #default sorting order for number is ascending order
# default sorting order for string is alphabetical order
# we should know that list should contain homogenious data otherwise we will get typeeerror
# python2 first short number then string follow

# for descending order
# mylist=[44,22,77,0,9,88]
# mylist.sort(reverse=True)
# print(mylist)

# to return the address of variable id function is used
# math =10
# print(id(math))

# math = 50
# phy = 50 #both will have same address
# print(id(math))
# print(id(phy))

# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

#two special type of membership operator : 1)in 2)not in
# name = 'Bhavika'
# print('v' in name) 

# name = 'Bhavika'
# print('v' not in name)

# for i in range(6):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(1,10,2): #increment by 2
#     print(i)

# for i in range(5,0,-1): #descending order
#     print(i)

# for i in range(5,0,-2): #decrement by 2
#     print(i)

# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end="\t")
# print()

# for i in range(1,11):
#         print(i*2," ",i*3," ",i*4)
#         print()

# no = int(input("Enter any digit: "))
# if no > 0:
#     print("Positive")
# if no < 0:
#     print('Negative')
# if no == 0:
#     print("Zero")

#WAP to accept days and check the working days and weekend
# days= input("Enter the day: ")
# if days == "SATURDAY" or "SUNDAY" or "saturday" or 'sunday':
#     print('Weekend!!!')
# else:
#     print("Workday.")

#WAP to accept three paper marks and calculate total,percentage and i f percentage is greater
# than equal to 60 then he/she is eligible for placement
# phy = int(input("Enter marks1: "))
# chem = int(input("Enter marks2: "))
# maths = int(input("Enter marks3: "))

# total = phy+chem+maths
# percentage = total/3.03

# if percentage >= 60:
#     print("Eligible for placement ")
# else:
#     print("Not eligible")

# WAP to accept 5 different values in 5 diffrenet variable and check maximun value and print
# by using simple if statement

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))
# d = int(input("Enter fourth value: "))
# e = int(input("Enter fifth value: "))

# if a > b and a > c and a > d and a > e:
#     print('a is greater', a)
# elif b > a and b > c and b > d and b > e:
#     print('b is greater', b)
# elif c > a and c > b and c > d and c > e:
#     print('c is greater', c)
# elif d > a and d > b and d > c and d > e:
#     print('d is greater', d)
# elif e > a and e > b and e > c and e > d:
#     print('e is greater', e)
# else:
#     print("There is a tie or equal values.")


