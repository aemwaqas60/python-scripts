def selection_sort(arr):  # Time complexity : O(n2)
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j

            arr[minIndex], arr[i] = arr[i], arr[minIndex]


myArray = [12, 2, 41, 5, 1, 55, 12, 22, 32]

print(f"\nSelection Sort :  ")
print(f"\nOriginal Array  : {myArray} ")

selection_sort(myArray)

print(f"\nSorted Array : {myArray}")
