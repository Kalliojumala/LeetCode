"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Constraints:

3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -10**4 <= target <= 10**4

"""
def threeSumClosest(nums, target):
    closest = 10**9
    ans = 0
    nums.sort()
    
    #same approach as in task 15: three_sum.py
    #this time we dont append results to a list but compare distances of the sums to the target and
    #return the sum with the closest distance
    for i in range(len(nums) - 2):
        pointer_low = i + 1
        pointer_high = len(nums) - 1
        
        while pointer_low < pointer_high:
            three_sum = nums[i] + nums[pointer_high] + nums[pointer_low]
            if(abs(target - three_sum) < closest):
                ans = three_sum
                closest = abs(target - three_sum)

            if three_sum < target:
                pointer_low += 1
            elif three_sum > target:
                pointer_high -= 1
            else:
                break
            
    return ans





if __name__ == '__main__':
    print(threeSumClosest([1,1,1,1], 0))