from lc136 import Solution
def main():
    nums = [2, 2, 1]
    nums1 = [4,1,2,1,2]
    nums2 =[1]

    print(Solution.findSingleOcurrance(nums, nums1, nums2))

    

if __name__ == 'main':
    main()

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1