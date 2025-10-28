class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mapp={}
        result,left=0,0
        arr=[]
        for i in s:
            arr.append(i)
        k=len(set(arr))
        if k==2 or k==1 or k==0:
            return 0
        for right,n in enumerate(s):
            if n in mapp:
                mapp[n]+=1
            else:
                mapp[n]=1
            while len(mapp)==k:
                result+=len(s)-right
                mapp[s[left]]-=1
                if mapp[s[left]]==0:
                    del mapp[s[left]]
                left+=1
        return result


