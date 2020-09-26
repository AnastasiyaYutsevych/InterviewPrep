#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
def containsDuplicate(nums):
    arr= []
    dupl = False
    for i in nums:
        if i in arr:
            dupl = True
        arr.append(i)
    return dupl


print(containsDuplicate([1,2,3,4]))