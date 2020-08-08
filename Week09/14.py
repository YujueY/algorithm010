class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = len(strs)
        if s == 1:
            return strs[0]
        n = len(min(strs))
        string = ""
        flag = True
        for j in range(n):
            if flag:
                for l in range(1, s):
                    if strs[l][j] == strs[l-1][j]:
                        if l == s-1:
                            string += strs[l][j]
                    else:
                        flag = False
                        break
        return string

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break           
        return s    

class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0
