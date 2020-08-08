class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return s
        a = list(s)
        n = len(s)
        for i in range(0, n, 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
