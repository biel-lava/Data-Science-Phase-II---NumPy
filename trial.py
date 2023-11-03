#print("elsa") # print tester

# Random array generator (integer)
''''
import random as rd

test_3d = [rd.randint(1, 100) for x in range(10)]

print(test_3d)
'''

'''
nums = [1,3,5,6]
target = 0


if target not in nums:
    target_index = 0
    for x in range(1, len(nums)):
        if ((nums[x-1]-target) < (nums[x]-target)) and ((nums[x]-target)<0):
            target_index = x + 1
        print(target_index)
else: 
    for num in nums:
        if target == num:
            print(f"Index of target: {nums.index(target)}")
'''