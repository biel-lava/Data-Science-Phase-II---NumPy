# Random array generator (integer)
''''
import random as rd

test_3d = [rd.randint(1, 100) for x in range(10)]

print(test_3d)
'''


nums = [0,0,1,1,1,1,1,1,2,2,3,3,4] # test array
aliens = [1, 4]
val = 1

for num in aliens:
    while num in nums:
        nums.remove(num)


print(nums)
