# arr = [2,3,2,4,2,5,7,5,7,8]
# minimum = min(arr) #find min and max range
# maximum = max(arr)

# size = maximum-minimum+1. # this is a frequency array of size range and we will store each element's frequency

# arr1 = []*(size)
# print(len(arr1))

# #step 3
# # make a prefix array of the frequency array and decrement one from each element


def countSort(arr,min,max):
    arr_range = max-min+1
    
    ans = [0]*len(arr)

    farr = [0]*arr_range

    for i in range (len(arr)):
        farr[arr[i]-min]+=1     #fill frequency array (step2)

    for i in range(1,len(farr)):
        farr[i] += farr[i-1]

    for i in range(len(arr)-1,-1,-1):
        pos = farr[arr[i]-min]-1
        ans[pos] = arr[i]
        farr[arr[i]-min] -=1    

    for i in range(len(arr)):
        arr[i] = ans[i]

    return ans

arr = [2,2,1,3,5,3,6,4,7,8,6]
min = min(arr)
max = max(arr)
sort = countSort(arr,min,max)
print(sort)