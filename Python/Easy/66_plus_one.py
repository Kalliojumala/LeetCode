def plusOne(digits: list):
    for i in range(-1, -len(digits) - 1, -1):
        if digits[i] + 1 < 10:
            digits[i] = digits[i] + 1
            return digits
        else:
            digits[i] = 0


def plusOne2(digits: list):

    x = 0
    num = 0
    for i in range(-1, -len(digits) - 1, -1):

        if x != 0:
            base = int("1" + (x * "0"))
        else:
            base = 1  
        
        num += digits[i] * base
        x += 1

    return [int(x) for x in str(num + 1)]


        


arr = [1,2,3]
x  = plusOne2(arr)
print(x)
