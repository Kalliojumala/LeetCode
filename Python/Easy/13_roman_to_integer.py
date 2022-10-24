"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Given a roman numeral, convert it to an integer.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

def solution_slow(s):
    #SLOOOOOOOOOOW.....
    table = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40,  'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500 , 'CM': 900, 'M':1000 }
    res = 0
    pointer = 0
   
    while pointer < len(s):
        if pointer+1 < len(s) and s[pointer] + s[pointer+1] in table:
            res += table[s[pointer] + s[pointer+1]]
            pointer += 2
            continue
        else:
            res += table[s[pointer]]
            pointer += 1

    return res
    

def solution(s):
    table = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40,  'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500 , 'CM': 900, 'M':1000 }
    res = 0
    for i in range(len(s)):
        if i != 0 and table[s[i-1]] < table[s[i]]: #if previous symbol was smaller we've "accidentally" added the previous instead of subtracting 
            res -= table[s[i-1]] * 2               #eg. i == D or 500 and i-1 is C or 100, CD equals 400 in roman and our total is 600 at that point.
        res += table[s[i]]                         #we correct this by subtracting i-1 * 2 from the total

    return res
if __name__ == '__main__':
    s = "MCMXCIV"
    print(solution(s))
    s = "III"
    print(solution(s))
    s = 'LVIII'
    print(solution(s))

