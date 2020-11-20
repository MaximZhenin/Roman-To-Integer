class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        answer, n = 0, len(s)
        for i, c in enumerate(s):
            v = roman[c]
            answer += -v if i < n-1 and v < roman[s[i+1]]  else v
        return answer