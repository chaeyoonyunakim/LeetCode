class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums:
                if i != nums.index(temp):
                    ans.append(i)
                    ans.append(nums.index(temp))
                    return ans
        