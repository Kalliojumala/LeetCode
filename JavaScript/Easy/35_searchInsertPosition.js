/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.  

Constraints:

    1 <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
    nums contains distinct values sorted in ascending order.
    -10**4 <= target <= 10**4

*/

//Basic approach
const searchInsert = (nums, target) => {

    //Given array is default sorted, if target is bigger than last element it goes to the end of the array.
    if(target > nums.slice(-1)) {
        return nums.length
    }

    for (let i = 0; i < nums.length; i++) {
        
        if (nums[i] === target || nums[i] > target) {
            return i
        }
    }
};

const nums = [1, 3, 5, 6]
console.log(searchInsert(nums, 7))