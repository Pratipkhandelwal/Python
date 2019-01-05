class Solution:
    def partition(self, s):
        s= "aab"
        self.res=[]
        self.findPalindrome(s,[])
        return self.res
    def findPalindrome(self,s,plist):
        if len(s)==0: self.res.append(plist)
        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.findPalindrome(s[i:],plist+[s[:i]])
    def isPalindrome(self,s):
        if s==s[::-1]:return True
        else: return False
