# # WAP to perform arithmetic operations using functional programming approach
# # Functions help us achieve modularity
# def addition(num1, num2):   # called function
#     print("Addition = ", num1 + num2)
# def subtraction(num1, num2):
#     print("Subtraction = ", num1 - num2)
# def multiplication(num1, num2):
#     print("Multiplication = ", num1 * num2)
# def division(num1, num2):
#     if num2 != 0:
#         print("Division = ", num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")
        
# while True:
#     print("\n--- Arithmetic Operations Menu ---")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice = int(input("Enter your choice from above options: "))
    
#     if choice == 5:
#         print("Exiting program...")
#         break
#     val1 = int(input("Enter First value: "))
#     val2 = int(input("Enter Second value: "))

#     if choice == 1:
#         addition(val1, val2)
#     elif choice == 2:
#         subtraction(val1, val2)
#     elif choice == 3:
#         multiplication(val1, val2)
#     elif choice == 4:
#         division(val1, val2)
#     else:
#         print("Invalid choice! Please select a valid option.")


#nested function

# def outerFunction():
#     print("This is my outer function:")
    
#     def innerFunction():
#         print("Inner function")    
#     innerFunction()     # calling the inner function
# outerFunction()        # calling the outer function


#input = bhavika is good programmer
#WAP to count the word
#output = 4

# name = "bhavika is good programmer"
# count = 1   
# for i in name:
#     if i == " ":
#         count += 1
#     else:
#         continue
    
# print("Total words =", count)


#MCQs

# init_tuple = ()
# print(init_tuple.__len__())

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a','b')
# print(init_tuple_a == init_tuple_b)

# init_tuple_a = '1', '2'
# init_tuple_b = ('3','4')
# print(init_tuple_a + init_tuple_b)

# l = [1,2,3]
# init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
# print(init_tuple)

# init_tuple = ('Python')*3
# print(type(init_tuple))

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1, 2),)* 7
# print(len(init_tuple[3:8]))


# s=""
# s1=s.replace("difficult","easy")
# print(s1)
# #All occurrences will be replaced 
# s="ababababababababab"
# s1=s.replace("a","b")
# print(s1)

#Removing spaces from the string:
#1.rstring()===> To remove space at right hand side
#2.lstring()===> To remove spaces at left hand side
#3.srtip()===> To remove spaces both sides
city=input("Enter your city Name:")
scity=city.strip()
if scity=="Hyderabad":
    print("Hello Hyderabadi..Adab")
elif scity=='Chennai':
    print("Hello Madrasi..Vanakkam")
elif scity=="Banglore":
    print("Hello Kannadiga..Subhodaya")
else:
    print("Your entered city is invalid")
