"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:

    3 <= nums.length <= 3000
    -10**5 <= nums[i] <= 10**5
"""

def solution_slow(nums: list) -> list: 
    result = []
    triplets = {}

    for i in range(len(nums)):
        for j in range(i + 1 , len(nums)):
            for x in range(j + 1, len(nums)):
                x = sorted([nums[i], nums[j], nums[x]])
                
                if sum(x) == 0 and (x[0], x[1], x[2]) not in triplets:
                    triplets[(x[0], x[1], x[2])] = x
                    result.append(x)

    return result

def solution(nums: list) -> list:
    print(sorted(nums))


if __name__ == '__main__':
    print(solution([-1,0,1,2,-1,-4]))
    #print(solution([1,1,1,1]))