'''
Chapter 4: NumPy Basics
Date: 10/24/23
Reference: Python for Data Analysis (McKinney, 2022)
Topics:
    1. 
'''

# NumPy ndarray basics
'''
import numpy as np

data = np.array([[15, 25, 23],[12, 45, 67]])

print(data) # simply print the data ndarray

print(data*10) # perfoms mathematical operation to the ndarray

print(data.shape) # gets the shape of the array
'''


# Transposing Arrays and Swapping Axes
#'''
import numpy as np

test_2d = np.array([[42, 13, 44],[63, 74, 93]])

test_swap = test_2d.reshape(2,3)
print(test_swap)

#'''

