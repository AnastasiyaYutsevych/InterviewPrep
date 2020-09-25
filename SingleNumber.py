#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
def singleNumber(arr):
    arr.sort()
    for i in range(0,len(arr)-1,2):
        if arr[i] != arr[i+1]:
            return arr[i]
    return arr[-1]


print(singleNumber([2,1,2]))
