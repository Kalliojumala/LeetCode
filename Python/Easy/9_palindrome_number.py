"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""

def solution_str(x: int) -> bool:
    if x < 0 or x % 10 == 0 and x != 0: #if x is negative it cannot be a palindrome, no number with trailing 0's except 0 can be a palindrome
        return False                    #eg. 10[::-1] == 01 == 1 and 1 != 10
    res = str(x)
    return res == res[::-1]             #if x passes conds, convert to str and compare to reversed string. 


def solution_int(x: int) -> bool:
    #solution without str conversion
    if x < 0 or x % 10 == 0 and x != 0: #same as in solution_str()
        return False
    original = x                        #copy of x, need x to compare res
    res = 0                                         
    while original > 0:
        res = res * 10 + original % 10  #orig % 10 equals tail number of orig|x, multiply current res and add tail until orig <= 0: 
        original = original // 10       #divide orig|x by 10 for next iter
                                        #example: orig|x == 12, res(0) * 10 + orig % 10 == 2 => res, orig // 10 == 1 => orig, after first loop res == 2, orig == 1 ->
                                        #         orig|x == 1, res(2) * 10 + orig % 10 == 1, 20 + 1 => res, orig // 10 == 0, second loop, res ==  21, orig == 0 and break ->
    
    return res == x


if __name__ == '__main__':
    print(solution_str(123))
    
    
    