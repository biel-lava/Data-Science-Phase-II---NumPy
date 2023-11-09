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

#Mk 1 Solution: Brute force approach
'''
nums = [1,3,5,6]
target = 2
target_index = 0

if target not in nums:
    for x in range(0, len(nums)):
        if ((nums[x-1]-target) < (nums[x]-target)) and ((nums[x]-target)<0):
            target_index = x
        print(target_index)
else: 
    for num in nums:
        if target == num:
            print(f"Index of target: {nums.index(target)}")
'''

# Mk 2: Binary search integration
''''
nums = [1,3,5,6]
target = 2

min_ind = 1
max_ind = len(nums)-1

if target in nums:
    print(nums.index(target))

if target < nums[min_ind-1]:
    print(f"Index of target: {min_ind-1}")

if target > nums[max_ind]:
    print(f"Index of target: {max_ind+1}")

else:
   curr_num = False
   while (min_ind <= max_ind and not curr_num):
        mid_ind = (max_ind + min_ind) // 2
        if nums[mid_ind] > target: #  cases na mas malaki yung mid element of array dun sa target na number
            max_ind = mid_ind - 1
        if nums[mid_ind] < target: # cases where mas maliit yung mid element of array dun sa target na number 
            min_ind = mid_ind + 1
        if nums[mid_ind-1]<target<nums[mid_ind]: # cases where in between na talaga yung target number
            curr_num = True
            print(f"Index of target: {mid_ind}")
'''

# Mk 3: Most efficient method (from solutions sa leetcode)
'''

nums = [1,3,5,6]
target = 7

low = 0
high = len(nums)


while low < high:
    mid = (high + low) // 2
    if target > nums[mid]:
        low = mid + 1 # magaadjust yung low index (increasing) until maging false na yung condition sa while 
    else:
        high = mid # oyherwise mauusog yung higher bounds for the index

print(low) 

'''




'''
Problem # 66: Plus one 
Date: 11/04/23
Link: https://leetcode.com/problems/plus-one/
Difficulty: Easy
Notes:  
    - Convert array into an integer, then add "1", then convert the sum into an array of integers
    - Helpful link: https://stackoverflow.com/questions/19599364/how-to-convert-array-of-integers-into-an-integer-in-c
'''

'''
digits = [1,2,3]
digit = ""

def convert(nums, digit): # converts the array of int into a single integer
    for x in nums:
        digit += str(x)
    return int(digit) + 1

def to_str(digits):
    sum = [int(x) for x in str(convert(digits, digit))]
    return sum


print(to_str(digits))

'''

'''
Problem # 88: Merge sorted array
Date: 11/07/23
Link: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Notes:  
    - Combine num1 and num2 arrays 
    - Ignore the 0 elements of the array
'''
# Mk 1 solution
'''
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [2,5,6]
n = 3

while nums1[len(nums1)-1] == 0: # checks if the last element of the array is still 0
    nums1.pop()
    if len(nums1) == 0:
            break
for x in nums2: # appends the non zero elements of nums2 to nums1
    if x != 0 and x != None:
        nums1.append(x)

while len(nums1)!= n+m:
    nums1.append(0)
nums1.sort()
print(nums1)
'''

# Mk 2 solution (from leetcode)
'''
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [2,5,6]
n = 3

a = m-1
b = n-1
write_index = m+n-1

while b >= 0: # backward approach, fills nums1 with the elements of nums2 from the last index position going forward sa unahan
		if a >= 0 and nums1[a] > nums2[b]: # checks if the last element of nums1 is 0
			nums1[write_index] = nums1[a] # if not zero ang ilalagay dun sa last element of updated nums1 ay yung last elemant of nums1
			a -= 1
		else:
			nums1[write_index] = nums2[b] # if zero nga then ang ilalagay would be yung last element of nums2
			b -= 1

		write_index -= 1


print(nums1)
'''


'''
Problem # 108: Conver Sorted Array to Binary Search Tree
Date: 11/09/23
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Difficulty: Easy
Notes:  
    - Root node is always 0
    - Sa left side lagi yung smaller value than the root node
    - Sa right side lagi yung larger value than the root node
'''