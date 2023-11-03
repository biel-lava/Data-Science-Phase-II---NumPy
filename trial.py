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
#'''
# first attempt for binary search
trial = [79, 64, 63, 95, 66, 5, 63, 76, 86, 78]

target = 76
min_ind = 0
max_ind = len(trial)-1

curr_num = False

while (min_ind <= max_ind and not curr_num):
    mid_ind = (max_ind + min_ind) // 2
    if trial[mid_ind] > target: #  cases na mas malaki yung middle element dun sa target na number
        max_ind = mid_ind - 1
    if trial[mid_ind] < target:
        min_ind = mid_ind + 1
    if trial[mid_ind] == target:
        curr_num = True
        print(f"Index of target: {mid_ind}")

#'''