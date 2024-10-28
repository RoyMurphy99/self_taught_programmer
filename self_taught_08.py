"""
chapter 8 exercises.
All exercises are in this file.
"""

# exercise 1
import statistics
nums = [1,2,3,4,5,6,7,8,9,10]
stan = statistics.stdev(nums)
print(stan)
print()

# exercise 2
import cubed
n = int(input("input number to cube: "))
ncubed = cubed.cube(n)
print(ncubed)
print()
