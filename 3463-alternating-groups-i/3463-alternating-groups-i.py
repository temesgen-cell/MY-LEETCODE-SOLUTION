class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n=len(colors)
        #since we need to check the first and the last lets make it circular
        colors+=colors
        result=0
        for i in range(n):
            if colors[i]==colors[i+2] and colors[i]!=colors[i+1]:
                result+=1
        return result



        