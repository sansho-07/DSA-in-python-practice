import sys
def radixSort(arr):
    max = -sys.maxsize - 1

    for i in range(len(arr)):
        if arr[i]>max:
            max = arr[i]

    exp = 1
    while exp<=max:
        count_sort(arr,exp)
        exp *=10

    return arr

def count_sort(arr,exp):
    arr_range = 10
    ans = [0]*len(arr)
    farr = [0]*arr_range

    for i in range(len(arr)):
        farr[(arr[i] // exp) % 10] += 1

    for i in range(1,len(farr)):
        farr[i] += farr[i-1]

    for i in range(len(arr)-1,-1,-1):
        position = farr[arr[i]//exp % 10]-1
        ans[position] = arr[i]
        farr[(arr[i] // exp) % 10] -= 1

    for i in range(len(arr)):
        arr[i] = ans[i]


arr = [232,121,453,234,332,643,332]
sort = radixSort(arr)
print(sort)