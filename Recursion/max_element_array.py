def max_element(arr,size,i,max):
    if size == i:
        return max

    if arr[i]>max:
        max = arr[i]

    return max_element(arr,size,i+1,max)

arr = [10,45,24,66,15]
size = len(arr)
max = float('-inf')

element = max_element(arr,size,0,max)

if element == -1:
    print("Something wrong")

else:
    print(" The max element is: ",element)
