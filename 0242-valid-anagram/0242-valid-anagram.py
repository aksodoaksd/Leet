class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}
        for i in s:
            if i in hashS:
                hashS[i] = hashS[i]+1
            else:
                hashS[i] = 1
        for i in t:
            if i in hashT:
                hashT[i] = hashT[i]+1
            else:
                hashT[i] = 1
        return hashS == hashT
        