"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Mapping: 1 = None, 2 = 'abc', 3 = 'def', 4 = 'ghi', 5 = 'jkl', 6 = 'mno', 7 = 'pqrs', 8 = 'tuv', 9 = 'wxyz'

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

"""


"""
a = 1,2 ab possibles are 1 3, 1 4, 2 3 or 2 4
b = 3,4 abc 1 3 5, 1 3 6, 1 4 5, 1 4 6, 2 3 5, 2 3 6, 2 4 5, 2 4 6      
c = 5,6


"""

from collections import deque
def solution(digits: str):
    if len(digits) < 1: #empty input returns empty array, no type checking required by assignment.
        return []

    #table to match digits to possible chars.
    table = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
        'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    muls = deque([]) #muls store multiplier value for result array and digits[i] to loop correct chars each iter
    possibilities = 1 #total number of possible combinations, eg input 23 has len(table[digits[0]]) * has len(table[digits[1]]) => 3 * 3 = 9 possibilities

    for i in digits:
        possibilities *= len(table[i]) 
        muls.append((i, len(table[i])))

    ans = [x for x in table[digits[0]]]
    muls.popleft()
    index = 0
    
    while len(ans) < possibilities:
        
        item, multiplier = muls.popleft() #get next char set and multiplier
        ans *= multiplier                 #multiply previous array by current multiplier [a,b,c] => [a,b,c,a,b,c,a,b,c] and sort
        ans.sort()
        
        for i in range(len(ans)):
            if index == len(table[item]): #loop current array assigning chars from table[item] eg. if item == 3, [a,a,a,b,b...] => [ad, ae, af...] 
                index = 0
            ans[i] = ans[i] + table[item][index]
            index += 1

    return ans


if __name__ == '__main__':
    print(solution("222"))  
    
    
