class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        from collections import defaultdict
        mapp=defaultdict(int)
        result,left=0,0
        k=len(set(nums))
        for right,n in enumerate(nums):
            mapp[n]+=1
            while len(mapp)==k:
                result+=len(nums)-right
                mapp[nums[left]]-=1
                if mapp[nums[left]]==0:
                    del mapp[nums[left]]
                left+=1
        return result

        


