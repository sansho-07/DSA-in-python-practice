def sorted_or_not(arr,size,i):

    if i == size -1 :           #it checks that until the last element of an array we have checked successfully.
        return 'sorted'
 
    if arr[i] > arr[i+1]:
        return 'not sorted'

    return sorted_or_not(arr,size,i+1)

arr = [23,42,45,53]
size = len(arr)
sorted_not = sorted_or_not(arr,size,0)

print(sorted_not)