class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        count0 = 0

        for i in nums:
            if i == 0:
                if count0 == 0:
                    count0 += 1
                else:
                    total = 0
                    break
            else:
                total *= i
        
        res = []
        for i in nums:
            if i == 0:
                res.append(total)
            elif count0 > 0:
                res.append(0)
            else:
                res.append((int) (total / i))
        
        return res
