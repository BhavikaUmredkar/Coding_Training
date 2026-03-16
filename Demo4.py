# Function
# def msg(): # called function
#     print("Hello World")  
# msg()


# def msg(): # called function
#     n1 = int(input("Enter the value of n1: "))
#     n2 = int(input("Enter the value of n2: "))
#     print("Add =", n1+n2)
# msg()


# how to return multiple value
# def opr():
#     n1 = int(input("Enter the value of n1: "))
#     n2 = int(input("Enter the value of n2: "))
#     sum = n1+n2
#     mul = n1*n2
#     sub = n1-n2
#     div = n1/n2
#     return sum,sub,mul,div #return in tuple. It is immutable
# result = opr()
# print(result)


# Four types of argument in python
# 1. Positional argument
# 2. Keyword argument
# 3. Default argument
# 4. Variable length argument/ variable number of argument 


# 1. Positional argument

# def personalInfo(fname, lname):
#     print("First Nmae=", fname)
#     print("Lat Name:", lname)
# personalInfo("Bhavika", "Umredkar")


# 2. Keyword argument

# def personalInfo(fname, lname):
#     print("First Nmae=", fname)
#     print("Lat Name:", lname)
# fname = "Bhavika"
# lname = "Umredkar"
# personalInfo(fname, lname)


# 3. Default argument

# def cityName(city="Nagpur"):
#     print(city)
# cityName("Mumbai")
# cityName("Pune")
# cityName()


# 4. Variable length argument/ variable number of argument 

def studentNames(*name):
    print(name)
studentNames("Bhavika","Bhumika","Rajeshri","Jims")

