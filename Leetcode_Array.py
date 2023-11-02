'''
LEETCODE ARRAY
Date: 10/31/23
Notes:
    - This is a dedicated file for playing with array problems from Leetcode
    - Basic progression would be puro easy muna then start dealing with the medium difficulties
'''



'''
Problem # 26: Removing Duplicates
Date: 10/31/23
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Notes:  
    - Make a function to return the number of unique numbers in the array as variable k
'''
'''
sample_array = [0,0,1,1,1,2,2,3,3,4] # test array

def count_dupli(arr):
    k = 1 # 1 as the default value since kahit isa lang naman yung element sa array considered pa rin yun as 1 unique element
    for x in range(1, len(sample_array)):
        if sample_array[x] != sample_array[x-1]: # checks if the current number is similar to the previous array (proper approach since if x+1 mageerror ulit as index out of range)
            k += 1
    return k
print(count_dupli(sample_array))
'''



'''
Problem # 27: Remove Element
Date: 11/02/23
Link: https://leetcode.com/problems/remove-element/
Difficulty: Easy
Notes:  
    - Given a value 'val' remove all occurance of val in the array
    - Return the updated length of array after removal as k
'''
'''
nums = [0,0,1,1,1,1,1,1,2,2,3,3,4] # test array
val = 1

while val in nums:
    nums.remove(val)

print(nums)

'''


'''
Problem # 35: Search Insert Position
Date: 11/02/23
Link: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
Notes:  
    - if target value is in array return the index
    - If target value not in array return the possible index na paglalagyan nung target value (in ascending order pa rin dapat)
'''









