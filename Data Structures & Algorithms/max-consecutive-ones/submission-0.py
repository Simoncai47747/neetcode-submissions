class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        currentNum = 0

        for i in nums:
            if i == 1:
                currentNum += 1
            else:
                currentNum = 0

            if currentNum > maxNum:
                maxNum = currentNum

        return maxNum
        