/*There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.  

Constraints:

    1 <= nums.length <= 5000
    -10**4 <= nums[i] <= 10**4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -10**4 <= target <= 10**4

*/

//Single pointer
const searchRotated = (nums, target) => {

    //Decide loops direction, given the array is semisorted
    if(nums[0] <= target) {
        for (let i = 0; i < nums.length; i++) {
            if(nums[i] === target) {
                return i
            }
        }
    }
    for (let i = nums.length - 1; i > 0; i--) {
        if(nums[i] === target) {
            return i
        }
    }

    return -1
}



