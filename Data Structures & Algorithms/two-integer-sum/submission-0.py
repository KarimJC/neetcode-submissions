class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 1

        seen = {}
        seen[nums[0]] = 0

        while True:
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i
            i += 1
            


            

