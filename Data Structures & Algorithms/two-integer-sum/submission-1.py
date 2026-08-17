class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 1

        seen = {}
        seen[nums[0]] = 0

        while True:
            comp = target - nums[i]
            if comp in seen:
                return [seen[comp], i]
            seen[nums[i]] = i
            i += 1
            


            

