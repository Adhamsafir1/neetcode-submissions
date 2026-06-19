class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for i in nums:
            if i-1 not in s:
                length = 1
                cur = i
                while cur+1 in s:
                    length+=1
                    cur+=1
                longest = max(longest , length)

        return longest
        