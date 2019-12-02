
def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)
        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex+1, lastIndex)
    else:
        return


def Partition(arr, firstIndex, lastIndex):
    i = firstIndex-1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[lastIndex] = arr[lastIndex], arr[i+1]
    return i


arr = [2, 3, 1, 6, 76, 56, 46, 88, 99, 43, 25]

print("initial array:\n", arr)
QuickSort(arr, 0, len(arr)-1)
print("result array:\n", arr)

