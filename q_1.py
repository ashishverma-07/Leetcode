class Solution:
    #def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def twoSum(self, nums, target):
            m = {}        
            for i in range (0, len(nums)):
                if nums[i] in m:
                    return [m[nums[i]],i]
                m[target-nums[i]]= i
            return []
