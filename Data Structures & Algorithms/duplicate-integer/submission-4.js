class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let set = new Set(nums)
        console.log(set)
        return set.size != nums.length
    }
}
