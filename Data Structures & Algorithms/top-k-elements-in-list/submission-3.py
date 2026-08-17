class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        solution = defaultdict(set)
        solution[1] = set()
        flipped = {}

        for n in nums:
            if n in flipped:
                solution[flipped[n]].remove(n)
                flipped[n] += 1
                if solution[flipped[n]]:
                    solution[flipped[n]].add(n)
                else:
                    solution[flipped[n]] = set()
                    solution[flipped[n]].add(n)
            else:
                solution[1].add(n)
                flipped[n] = 1
        
        sortedKeys = sorted(solution.keys(), reverse=True)

        result = []
        i = 0
        while len(result) < k:
            if len(result) + len(solution[sortedKeys[i]]) <= k:
                result.extend(solution[sortedKeys[i]])
                i += 1
            else:
                result.extend(list(solution[sortedKeys[i]])[:k - i + 1])
                break
            
        return result
            
            