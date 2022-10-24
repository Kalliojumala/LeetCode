"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Constraints:

    1 <= num <= 3999

"""


def solution(x: int):
    table = {1: 'I', 4: 'IV', 5: 'V', 9:'IX', 10: 'X', 40:'XL',  50: 'L', 90:'XC', 100: 'C', 400:'CD', 500: 'D', 900:'CM', 1000: 'M', }
    res = ""
    for i in range(len(str(x))):
        pointer = str(x)[0] 
        trails = '0' * (len(str(x)) -1)
        first_num = int(pointer + trails) #lead number eg. x = 1996 => pointer = 1000

        if first_num in table: 
            res = res + table[first_num]  #if first_num is convertable straight away from table, add symbol to res and set x to x - first_num
            x -= first_num
            continue

        else:
            y = int("1" + trails)       #step to make loop faster, ex if first_num is 300 we want to go down 100 steps at a time not 1
            copy_first = first_num      #copy first_num, need it for remainder calc 
            while first_num != 0:       #loop until whole number is converted, -y from copy_first until match, set symbol to res and -copy_first from first_num
                                        #eg first_num = 700, match comes at 500, save symbol of 500('D') and repeat loop for remainder (700 - 500) until remainder is 0
                if copy_first in table:
                    res = res + table[copy_first]  #
                    x -= copy_first
                    first_num -= copy_first 

                    if first_num == y:
                        res = res + table[first_num] 
                        x -= first_num
                        break

                    copy_first = first_num 
                    
                copy_first -= y 
        
    return res

def solution_2(x: int):
    #more optimized solution using stack (about 2 times faster)
    stack = [(1,'I'), (4,'IV'), (5,'V'), (9,'IX'), (10,'X'), (40,'XL'),  (50,'L'), (90,'XC'), (100,'C'), (400,'CD'), (500,'D'), (900,'CM'), (1000, 'M')]
    res = ""
    while x > 0:
        if x - stack[-1][0] >= 0:       #if stack[-1] value is larger than x, it will not be needed anymore
            res = res + stack[-1][1]    #compare largest value in stack, if it 'fits' add corresponding symbol to res
            x -= stack[-1][0]
        else:
            stack.pop()
    
    return res

num = 2994
solution_2(1994)



