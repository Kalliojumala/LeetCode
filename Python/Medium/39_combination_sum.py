"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


"""

class Solution:
    

    def combinationSum(candidates, target):
        ans = []
        curr_item = [0 for x in range(target // min(candidates) + 1)]
        candidates.sort()

        def helper(candidates, target, start, ans, curr_item, current=0, index=0):
            if current == target:
                ans.append(curr_item[:index])

            for i in range(start, len(candidates)):
                if current + candidates[i] <= target:
                    
                    curr_item[index] = candidates[i]
                    helper(candidates, target, i, ans, curr_item, current + candidates[i],index +1)
                else:
                    return
        helper(candidates, target, 0, ans, curr_item)
        
        return ans


if __name__ == '__main__':
    print(len(Solution.combinationSum([x for x in range(1, 10**9)], 11)))