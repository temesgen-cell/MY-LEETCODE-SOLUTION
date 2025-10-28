class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result,left=0,0
        window=arr[:k]
        summ=sum(window)
        if summ//k >= threshold:
            result+=1
        for right in range(k,len(arr)):
            summ+=arr[right]
            summ-=arr[left]
            if summ //k >= threshold:
                result+=1
            left+=1
        return result