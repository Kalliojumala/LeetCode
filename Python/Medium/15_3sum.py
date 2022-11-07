"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:

    3 <= nums.length <= 3000
    -10**5 <= nums[i] <= 10**5
"""


def solution(nums: list) -> list:
    duplicates_fixed = set()
    ans = []
    nums.sort()

    #base case
    #no sum of 3 can equal 0 with only positive integers or array that has fewer than 3 elements
    if nums[0] > 0 or len(nums) < 3:
        return ans                   

    #two pointer approach
    for i in range(len(nums)):
        pointer_low = i + 1
        pointer_high = len(nums) - 1
        
        if nums[i] in duplicates_fixed:
            continue

        #base case again
        if nums[i] > 0:
            break

        while pointer_low < pointer_high:
            three_sum = nums[i] + nums[pointer_low] + nums[pointer_high]
            
            #if sum is smaller than zero we need bigger total, increase low pointer
            if three_sum < 0:
                pointer_low += 1
            #if sum bigger we need to decrease our high pointer
            elif three_sum > 0:
                pointer_high -= 1
            else:
                #when a match is found append the triplet to answer array                
                ans.append([nums[i], nums[pointer_low], nums[pointer_high]])

                #save last used pointers to avoid duplicates. 
                last_low, last_high = nums[pointer_low], nums[pointer_high]

                #modify pointers until they point at a different value than what was added
                #if pointers 'cross' while loop gets broken, start next iteration
                while pointer_low < pointer_high and nums[pointer_low] == last_low:
                    pointer_low += 1
                while pointer_low < pointer_high and nums[pointer_high] == last_high:
                    pointer_high -= 1

        #prevent fixed value from being used again.
        duplicates_fixed.add(nums[i])

    return ans






if __name__ == '__main__':
    print(solution([-1,0,1,2,-1,-4]))
    #print(solution([1,1,1,1]))