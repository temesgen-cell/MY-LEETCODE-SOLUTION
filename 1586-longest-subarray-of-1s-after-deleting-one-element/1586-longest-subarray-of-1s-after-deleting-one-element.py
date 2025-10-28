class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sumi = 0
        container = []
        # Count consecutive 1s between zeros
        for i in nums:
            if i == 1:
                sumi += 1
            else:
                container.append(sumi)
                sumi = 0
        # Append last streak if array ends with 1s
        container.append(sumi)

        # all ones — must delete one element
        if len(container) == 1 and 0 not in nums:
            return container[0] - 1

        # all zeros
        if max(container) == 0:
            return 0

        #  only one zero (two groups of 1s)
        if len(container) == 1:
            return container[0]

        # Now combine groups separated by a single zero
        max_len = 0
        for i in range(len(container) - 1):
            # Adjacent streaks are separated by exactly one zero
            max_len = max(max_len, container[i] + container[i + 1])
        
        return max_len
