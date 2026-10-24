class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        item_counts = {}
        for item in nums:
            if item in item_counts:
                item_counts[item] += 1
            else: 
                item_counts[item] = 1 

        for key in item_counts: 
            if item_counts[key] >= 2:
                return True

        return False