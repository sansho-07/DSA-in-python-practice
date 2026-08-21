def binarySearch(arr,key):
    beg = 0
    end = len(arr)-1

    while beg<=end:
        mid = (beg+end)//2

        if key == arr[mid]:
            return f"The element {key} is found at {mid}."
        
        if key>arr[mid]:
            beg = mid+1

        else:
            end = mid-1


arr = [23,34,45,67,89,90]
key = int(input("Enter a number to search for: "))
result = binarySearch(arr,key)
print(result)

