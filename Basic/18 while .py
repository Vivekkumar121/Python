# x = int(input("enter the last number "))
# a = 1
# while(x > 0) :
#     a = a * x
#     x = x - 1
# else : 
#     print("the factorial of x is ",a)
    
# #                                                                   /*Do-WHile
# i = 0
# while True :
#     print(i)
#     i = i + 1
#     if(i % 50 == 0) :
#         break
# #                                                                    Do while
# s = 0
# do : print(i)
# i = i+ 1
# while(i < 15):

# defining list of strings
list1 = ["geeksforgeeks", "C++",
		"Java", "Python", "C", "MachineLearning"]

# initialises a variable
i = 0

print("Printing list items\
using while loop")
size = len(list1)
# Implement while loop to print list items
while(i < size):
	print(list1[i])
	i = i+1

i = 0

print("Printing list items\
using do while loop")

# Implement do while loop to print list items
while(True):
	print(list1[i])
	i = i+1
	if(i < size and len(list1[i]) < 10):
		continue
	else:
		break
