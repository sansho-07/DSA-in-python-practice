def merged_sort(arr1,arr2,arr):
    i = j = k = 0

    while i<len(arr1) and j<len(arr2):

        if arr1[i]<arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1

    while i< len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1

    while j<len(arr2):
        arr[k] = arr2[j]
        j+=1
        k+=1

    return

def sortArray(arr):

    if len(arr)<=1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    sortArray(left)
    sortArray(right)

    merged_sort(left,right,arr)

array = [2,3,1,6,4,8,5,9]
sortArray(array)
print(array)