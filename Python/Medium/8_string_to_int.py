#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
import time 

def solution(s: str):
    nums = '0123456789'
    res = 0
    neg = False
    start = True
    s = s.strip()
    
    for i in s:
        if start:
            if i == '-':
                start = False
                neg = True
                continue
            elif i == '+':
                start = False
                continue

        if i in nums:
            start = False
            res = res * 10 + int(i)
        else:
            break
    
    if neg:
        return max(-2**31, -res)
    
    return min(2**31-1, res)
   
    

    


if __name__ == '__main__':
    s = '      -42923843'
    start = time.time()
    print(solution(s))
    end = time.time()
    print(end-start)
    