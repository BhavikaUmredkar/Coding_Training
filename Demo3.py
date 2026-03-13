# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# for i,j in zip(range(1,6),range(5,0,-1)):  
#     if i ==3 and j ==3:
#         continue
#     print(i," ",j)

#while
# i=1
# while i<=5:
#     print(i)
#     i =+1

# username =''
# password =''
# while username != "admin" and password != "hello":
#     username = input("Enter username:")
#     password = input("Enter password:")

# n = int(input("Enter number:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+1
#     i=i+1
#     print("The sum of first",n,"numbers is:",sum)

# name ="bhavika"
# newname=" "
# for i in name:
#     if i not in newname:
#         newname +=i
# print(name)
# print(newname)

# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i >400:
#         print("Item:")
#         continue
#     print(i)
    
#Palindrome:

# name="racecar"
# if name == name[::-1]:
#     print("palindrome string")
# else:
#     print("not palindrome")


#ANAGRAM
# string1 = input("enter string 1:")
# string2= input("enter string 2:")

# if(len(string1) and len(string2)):
#     print("anagram")
# else:
#     print("not anagram")


#Remove key value pair from dictionary
# mydict={
#     "name":"bhavika",
#     "age":19
# }
# mydict["mobile_no"]=89387373793
# print(mydict)

# mydict.pop("age")
# print(mydict)

# print(mydict.get("name"))


#nested loop
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print( )



n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(64 + j), end=" ")
    print()
# A B C D 
# A B C D
# A B C D
# A B C D

print("---------------")
n = int(input(" enter the no of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i, end=" ")
    print()
# 4 4 4 4 
# 3 3 3 3
# 2 2 2 2
# 1 1 1 1