#Given an array, rotate the array to the right by k steps, where k is non-negative.
def rotate(nums,k):
    nums.reverse()
    if k> len(nums):
        k = k-len(nums)
    nums[:k] = nums[:k][::-1]
    nums[k:]= nums[k:][::-1]
nums = [1,2]
rotate(nums,3)
print(nums)
nums =[1,2,3,4,5,6,7]
rotate(nums,3)
print(nums)

