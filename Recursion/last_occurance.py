def last_occurance(arr,size,i,val):
    if size==i:
        return -1

    if arr[i]==val:
        return i

    return last_occurance(arr,size,i-1,val)

arr = [1,2,2,3,4]
size = len(arr)
val = int(input("Enter a value: "))

index = last_occurance(arr,size,size-1,val)

if index !=-1:
    print(f"The {val} is found at {index}")

else:
    print(f"The {val} is not found in an array")