# Random array generator (integer)
''''
import random as rd

test_3d = [rd.randint(1, 100) for x in range(10)]

print(test_3d)
'''


sample_array = [0,0,1,1,1,2,2,3,3,4]
k = 1

#'''
for x in range(1, len(sample_array)-1):
    if sample_array[x] != sample_array[x-1]:
        sample_array.pop()
#'''


print(sample_array)

