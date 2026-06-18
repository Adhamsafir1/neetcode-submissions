class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def rec1(l,prod):
            if len(l)>1:
                return [0]*len(nums)
            ans = [0]*len(nums)
            ans[l[0]] = prod
            return ans

        def rec2(prod):
            ans = [prod]*len(nums)
            for i in range(len(nums)):
                ans[i] = ans[i]//nums[i]
            return ans
        l = []
        prod = 1
        for i in range(len(nums)):
            if nums[i]==0:
                l.append(i)
                continue
            prod*=nums[i]
            
        
        if l:
            return rec1(l , prod)
        else:
            return rec2(prod)
        

        