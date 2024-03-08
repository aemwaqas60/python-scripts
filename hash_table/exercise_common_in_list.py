# This method will find the common number in two different list using the nested for
# Time complexity :  O(n2)
def common_in_lists(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


# This method will find the common number in two different list using the nested for
# Time complexity :  O(n)
def common_in_lists_using_dict(list1, list2):
    myDict = {}
    for i in list1:
        myDict[i] = True
    for j in list2:
        if j in myDict:
            return True
    return False


myList1 = [1, 3, 4, 5, 6, 7]
myList2 = [11, 13, 14, 15, 16, 17]

print(f'find common in list using for loop : {common_in_lists(myList1, myList2)}')
print(f'find common in list using for dict : {common_in_lists_using_dict(myList1, myList2)}')
