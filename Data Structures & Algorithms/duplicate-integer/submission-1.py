class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSoFar = []

        for i in nums:
            if i in seenSoFar:
                return True
            
            seenSoFar.append(i)

        return False
        