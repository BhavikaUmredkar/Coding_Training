# fruit_list1 = ["Apple", "Berry", "Cherry", "Papaya"]

# fruit_list2 = fruit_list1          # same reference
# fruit_list3 = fruit_list1[:]       # copy

# fruit_list2[0] = "Guava"
# fruit_list3[1] = "Kiwi"

# sum = 0

# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == "Guava":
#         sum += 1
#     if ls[1] == "Kiwi":
#         sum += 20

# print(sum)



# def func(value, values): # value = 3 and values =[1,2,3]
#     var = 1
#     values[0] =44 #[44,2,3]
# t = 3
# v =[1,2,3]
# func(t,v)
# print(t,v[0])


# fruit= {}
# def addone(index):
#     if index in fruit:
#         fruit[index] +=1
#     else:
#         fruit[index] =1 #{'Apple}:1, 'banana':1, 'apple':1}
        



# #given an array return an array where each element is the product of all the elements in the array except itself
# #logic  use two passes one from left to right and one from r to l to calculate product
# # input [1,2,3,4] output [ 24,12,8,6]

# def product(nums):
#     n = len(nums)
#     result = []

#     for i in range(n):
#         prod = 1
#         for j in range(n):
#             if i != j:
#                 prod *= nums[j]
#         result.append(prod)

#     return result


# print(product([1, 2, 3, 4]))  # [24, 12, 8, 6]