"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
"""

class Solution:
    def firstMissingPositive(nums: list) -> int:
        nums.sort()
        hash = {}
        missing = 1
        for i in nums:
            if i > 0:
                if i != missing and i not in hash:
                    return missing

                if i not in hash:
                    hash[i] = 1
                    missing += 1

        return missing

    def firstMissingPositive_2(nums: list) -> int:
        hash = set()
        
        for i in nums:
            if i > 0 and i not in hash:
                hash.add(i)
            
        
        for i in range(1,len(nums) + 1):
            if i not in hash:
                return i

        return max(nums) + 1
        



if __name__ == '__main__':
    print(Solution.firstMissingPositive_2([2]))
    print(Solution.firstMissingPositive_2([3,4,-1,1]))
    print(Solution.firstMissingPositive_2([1,1,2,2,4,7]))

    