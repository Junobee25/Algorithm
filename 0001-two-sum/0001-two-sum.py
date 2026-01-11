class Solution(object):
    def twoSum(self, nums, target):
        set_dict = {}
        arr_length = len(nums)
        result = []
        for i in range(arr_length):
            if target - nums[i] in set_dict:
                return [set_dict[target-nums[i]],i]
            set_dict[nums[i]] = i

            
            


        