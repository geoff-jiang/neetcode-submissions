class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let m = new Map();

        for (let i = 0; i< nums.length; i++) {
            if (!m.has(nums[i])) {
                m.set(nums[i], i);
            }
            else{ 
                return true;
            }
            
        }
        return false
    }
}
