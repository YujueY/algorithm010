def numDecodings(s: str) -> int:
    pre = 1
    cur = 1
    if s[0] == "0":
        return 0
    for i in range(1, len(s)):
        if s[i] == "0":
            if s[i - 1] == "1" or s[i - 1] == "2":
                cur = pre
            else:
                return 0
        else:
            if s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                temp = cur
                cur += pre
                pre = temp
            else:
                pre = cur
                cur = cur

    return cur
