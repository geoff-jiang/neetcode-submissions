

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for (let i = 0; i < nums.length; i++) {
            let rem = nums.findIndex((e) => e == (target - nums[i]))
            if (rem != i && rem != -1) {
                return [i, rem]
            }
        }
    }
}
