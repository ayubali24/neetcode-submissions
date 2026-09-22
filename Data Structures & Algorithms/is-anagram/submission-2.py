class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

        for j in range(len(t)):
            if t[j] in t_dict:
                t_dict[t[j]] += 1
            else:
                t_dict[t[j]] = 1
        if len(s_dict) != len(t_dict):
            return False

        
        for x in s_dict:
            if x not in t_dict:
                return False
        
        for x in s_dict:
            if s_dict[x] != t_dict[x]:
                return False
        
        return True