class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i = 0
        j = len(heights)-1
        while i<j:
            a = heights[i]
            b = heights[j]
            min_h = min(a,b)
            ans = max(ans , min_h*(j-i))
            if a<b:
                i+=1
            else:
                j-=1
        return ans

        