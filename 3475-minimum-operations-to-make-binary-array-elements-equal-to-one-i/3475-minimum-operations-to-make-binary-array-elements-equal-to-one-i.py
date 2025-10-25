class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for right in range(len(nums)-2):
            if nums[right]==0:
                nums[right]=1
                nums[right+1]=1-nums[right+1]
                nums[right+2]=1-nums[right+2]
                count+=1
        for i in range(len(nums)):
            if nums[i]==0:
                return -1
        return count

        