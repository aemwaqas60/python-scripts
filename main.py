# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# def sortedSquares(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     for index, item in enumerate(nums):
#         print(f"Index : {index} :  abs value : {abs(nums[index])}")
#         nums[index] = abs(nums[index])
#         nums[index] = nums[index] * nums[index]
#         # nums.sort()
#
#     print(nums)


l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)


# print("Return type:", type(obj1))
# print(list(enumerate(l1)))

# changing start index to 2 from 0
# print(list(enumerate(s1, 2)))


# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i, item in enumerate(nums):
#         print(f'i : {i}')
#         for j in range(i + 1, len(nums)):
#             print(f'j : {j}')
#             if target == nums[i] + nums[j]:
#                 return [i, j]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for a in range(len(nums)):
        ans = target - nums[a]
        # print(ans)

        print(nums[a])
        if nums[a] in d:
            return [a, d[nums[a]]]
        # print ('yes')
        else:
            d[ans] = a
            print(d)


list1 = [2, 4, 5, 8, 2, 6, 7]
output = twoSum(list1, 10)

print(f"output : {output}")


def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    current = list1
    if list1:
        while current:
            if current.next is None:
                break
            current = current.next

    if current:
        current.next = list2
    if list1:
        current = list1
        while current:
            current1 = list1
            while current1:

                if current1.value < current.value:
                    temp = current.value
                    current.value = current1.value
                    current1.value = temp

                current1 = current1.next

            current = current.next

    return list1


list1 = []
