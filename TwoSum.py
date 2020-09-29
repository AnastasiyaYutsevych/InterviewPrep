#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.
def twoSum(nums, target):
    for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nums[i+1:]:
                return [i, nums.index(needed, i+1)]
    
print(twoSum([0,4,3,0],0))
print(twoSum([0,-1,-2,-3,-5],-8))

