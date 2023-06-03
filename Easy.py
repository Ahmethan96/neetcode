Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
###################################################################################################################################################
My solution: 
###################################################################################################################################################
# nums = [1,2,3,4]
nums = [1,2,3,1]
# nums = [1,1,1,3,3,4,3,2,4,2]
# test = nums[-1]
# print(test)

def check_duplicates():

    for i in range(len(nums)):
        print(nums[i])
        print(nums[i + 1:len(nums)])
        if nums[i] in nums[i+1:len(nums)]:
            return True
        else:
            return False
print(check_duplicates())

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

#######################################################################################################################################################
My solution:
#######################################################################################################################################################
nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

def check_target():
    for i in ((nums)): # start 2, 7, 11, and 15
        for j in ((nums)): # start
            if nums.index(i) != nums.index(j):
                if i + j == target:
                    return nums.index(i), nums.index(j)
   
