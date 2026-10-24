class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        returnList = []
        for i in range(0,len(nums)):
            diff_map[nums[i]] = i
        
        for i in range(0,len(nums)):
            difference = target - nums[i]
            if difference in diff_map and diff_map[difference] != i:
                returnList.append(i)
                returnList.append(diff_map[difference])
                return returnList
            
            
        

        