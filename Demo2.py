#WAP to accept three paper marks and check maximum marks using nested if else
#Nested if else:

# mark1 = int(input("Enter marks of Paper 1: "))
# mark2 = int(input("Enter marks of Paper 2: "))
# mark3 = int(input("Enter marks of Paper 3: "))

# if mark1 >= mark2:
#     if mark1 >= mark3:
#         print("Maximum marks are:", mark1)
#     else:
#         print("Maximum marks are:", mark3)
# else:
#     if mark2 >= mark3:
#         print("Maximum marks are:", mark2)
#     else:
#         print("Maximum marks are:", mark3)


# else if ladder
# if condition:
#     #statement
# elif condition:
#     #satement
# else:
#     #default block 

#WAP to accept percentage and if per
# per = float(input("Enter your percentage: "))

# if per > 90:
#     print("Grade: A")
# elif per > 80:
#     print("Grade: B")
# elif per > 60:
#     print("Grade: C")
# else:
#     print("Grade: Fail")

#indexing and slicing is not possible in dictionary
# mydict = {
#     "name": "Bhavika",
#     "professional": "Student",
#     "empid":1001
# }
# print(mydict)
# print(type(mydict))
    
# mydict = {
#     101: "Bhavika",
#     102: "Ashish",
#     "103": "Mohini",
#     "104": "Avni",
#     101: "Ashish",
#     104: "Ashwini"
# }
# print(mydict)
# a = mydict[102]
# print(a)

# #replace old value by new
# mydict[102] = "peter"
# print(mydict)

# # only print key x=0,1
# for x in mydict:
#     print(x)

# # only print values
# for x in mydict.values():
#     print(x)
    
# # Printing key and values both
# for x,y in mydict.items():
#     print(x,y)
    
#if i have to add new key and value pair in my dictionary
# mydict["mobile_no"]=457890
# print(mydict)

# mydict["Department"] = "management"
# print(mydict)

# mydict = {
#     101: "Bhavika",
#     "professional": "Student",
#     "empid": 1001
# }
# mydict.pop(101)
# print(mydict)
#pop() method remove pair by specific key name


#SLICING
# name="BhavikaUmredkar"

#indexing= 01234567890
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

# s = "help4code is a best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))

# s = "bhavika","nishika","bhumika"
# m = '|'.join(s)
# print(m)

# s= "Python is a high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print('Subject Marks:')
# phy = 50
# chem = 60
# math = 70

# print("physics ={} chemistry={} Math={}".format(phy,chem,math))
# print("physics ={0} chemistry={1} Math=(2)".format(phy,chem,math))
# print("physics ={x} chemistry={y} Math={z}".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks", f"{total} ")
# print("Roll No=", "7".zfill(4))

# print('prashantjha777'.isalnum())        # True → all letters and digits
# print('prashantjha'.isalpha())           # True → all letters
# print('777f'.isdigit())                  # False → contains 'f'
# print('sdsdsdsd'.islower())              # True → all lowercase
# print('abc'.islower())                   # True
# print('PRASHANTj'.isupper())             # False → contains lowercase 'j'
# print('My Name Is Prashant'.istitle())   # True → each word starts uppercase
# print('.'.istitle())                     # False → '.' is not title case
# print('   '.isspace())                   # True → only spaces
# print("Hello".startswith("He"))          # True → starts with "He"
# print("Hello".endswith("lo"))            # True → ends with "lo"

#BOADMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

# name = 'bhavika'
# for i in name:
#     print(i) #i=1/2/3/4/5/6/7

name = 'bhavika'
data = ['a','e','i','o','u']
vowel =0
con =0
for i in name:
       if i in data:
              vowel +=1
              
       else:
              con +=1
print('vowel count:', vowel)
print('consonent count:', con)


s = 'programming'
duplicates=[]
for i in s:
       if name.count(s) > 1 and s not in duplicates:
        duplicates.append(ch)

print("Duplicate characters:", duplicates)
    
