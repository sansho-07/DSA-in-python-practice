def printArray(arr,size,i,val):
    if i==size:
        return -1 

    if arr[i]==val:
        return i

    return printArray(arr,size,i+1,val)

arr = [1,2,2,3,4,4]
size = len(arr)
val = int(input("Enter a number that you want to find: "))

index = printArray(arr, size, 0, val)

if index!=-1:
    print(f"The {val} is found at {index}")

else:
    print(f"the {val} is not in an array")