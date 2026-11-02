class Solution(object):
        def twoSum(self, nums, target):
            targets = {}
            for index, num in enumerate(nums):
                targets[num] = index

            for index, num in enumerate(nums):
                pair_index = targets.get(target - num)
                if pair_index is not None and pair_index != index:
                    return [index, pair_index]
                
