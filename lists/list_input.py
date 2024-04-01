list1 = []
# get a list from user as input using list comprehension

# list1 = [int(item) for item in input("Enter you list items : ").split()]
# list2 = [item for item in input("Enter you list items : ").split()]
#
# print(f'List 1 : {list1}')
# print(f'List 2 : {list2}')


# Get a list as input from user with for loop

n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list1.append(ele)
print(f'List : {list1}')

# Get a list as input from user with exception handling

# try:
#     list1 = []
#     while True:
#         element = int(input())
#         list1.append(element)
# # print the list if the use does not enter the integer value
# except:
#     print(list1)
