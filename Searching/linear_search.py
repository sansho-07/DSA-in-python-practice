def linearSearch(arr,target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return f"the element {target} is found at {i}."

    
    return f"the element {target} is not present in array."
        

arr = [43,24,24,64,33,65,87]
target = 64
found = linearSearch(arr,target)
print(found)