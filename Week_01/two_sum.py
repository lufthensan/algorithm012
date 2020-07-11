class Solution:
    def twoSum(self, nums, target) :
        map={}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target -nums[i]] = i
            else:
                return map[nums[i]],i
        return -1,-1

    # def twoSum(self,nums,target):
    #     for i in range(len(nums)):
    #         if((nums.index(target - nums[i]) != -1) and (nums.index(target - nums[i]) != i)):
    #             return i,nums.index(target-nums[i])
    #         else:
    #             continue
    #     return -1,-1
        