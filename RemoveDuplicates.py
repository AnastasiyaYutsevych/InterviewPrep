#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

def remove(arr):
    i = 1
    while i < len(arr):
        if arr[i-1] == arr[i]:
            print(arr, i)
            arr.pop(i-1)
            i-=1
        i+=1
    return arr

print(remove([0,0,1,1,1,2,2,3,3,4]))

