class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
             return len(nums)
        tag_front, tag_back = 0,1
        while tag_back != len(nums):
            if nums[tag_front] == nums[tag_back]:
                nums.pop(tag_back)
            else:
                tag_front += 1
                tag_back += 1
        return len(nums)

            