#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

#lazy python sol...
def solution_str(x: int):
    str_x = str(x)[::-1]
    sol = 0
    if x < 0:
        sol = int("-" + str_x[0:-1])
    else:
        sol = int(str_x)
    
    return sol if abs(sol) < 2**31 - 1 else 0 

    




if __name__ == '__main__':
    x = 4562
    print(solution_str(x))
    x = -123
    print(solution_str(x))
    x = 120
    print(solution_str(x))

    print(2**31 -1 , -2**31)