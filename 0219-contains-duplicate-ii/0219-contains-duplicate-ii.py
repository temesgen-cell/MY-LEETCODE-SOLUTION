class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowCollector=set()
        for i in range(len(nums)):
            if i>k:
                windowCollector.remove(nums[i-k-1])
            if nums[i] in windowCollector:
                return True
            windowCollector.add(nums[i])
        return False