from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        step = 1
        for index, number in enumerate(nums):            
            for idx, nw in enumerate(nums[step:]):                
                if number + nw == target:
                    return index, idx + step
            step += 1
