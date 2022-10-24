"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""


def solution_o2(strs): 
    max_len = len(strs[0])
    prefix = ""
    for i in strs:
        max_len = min(max_len, len(i)) #prefix cant be longer than a word in the list

    for i in range(max_len):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[j-1][i]: #matches every index to other words, if one 'misses' return current prefix.
                return prefix
        prefix = prefix + strs[0][i]
    
    return prefix

def solution(strs):
        
    if len(strs) == 0:
        return '' 
    res = ''
    strs = sorted(strs)
    for i in range(len(strs[0])):
        if strs[-1][i] == strs[0][i]:
            res += strs[0][i]
        else:
            break
    return res



if __name__ == '__main__':
    strs = ["aabc","aab","aac"]
    print(sorted(strs))
    print(solution(strs))
    