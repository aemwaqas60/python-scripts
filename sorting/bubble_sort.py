def bubble_sort(arr):  # Time complexity : O(n*(n-1)/2)
    arrLength = len(arr)

    for i in range(arrLength):
        for j in range(0, (arrLength - i) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    # base case
    if n == 1:
        return
    count = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            count += 1

    if count == 0:
        return
    bubble_sort_recursive(arr, n - 1)


myArray = [12, 1, 3, 44, 55, 6, 10, 19, 18, 4]
myArray1 = [12, 1, 3, 44, 55, 6, 10, 19, 18, 4]

print(f"\nBubble Sort : ")
print(f"\nOriginal Array  : {myArray}")
bubble_sort(myArray)
bubble_sort_recursive(myArray1)
print(f"sorted Array Using iteratively  : {myArray}")
print(f"sorted Array Using recursively  : {myArray1}")
