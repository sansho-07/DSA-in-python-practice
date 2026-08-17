def max_element(arr,size,i,min):
    if size == i:
        return min

    if arr[i]< min:
        min = arr[i]

    return max_element(arr,size,i+1,min)

arr = [10,45,24,66,5]
size = len(arr)
min = float('inf')

element = max_element(arr,size,0,min)

if element == -1:
    print("Something wrong")

else:
    print(" The max element is: ",element)
