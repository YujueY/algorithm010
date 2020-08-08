class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split()
        return len(string[-1]) if string else 0

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        if not s and len(s) == 0:
            return 0
        count = 0
        for i in s[::-1]:
            if i == " ":
                if count == 0:
                    continue
                else:
                    break
            else:
                count += 1
            
        return count

