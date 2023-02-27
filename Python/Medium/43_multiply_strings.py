def multiply(num1: str, num2: str):
    if type(num1) != str or type(num2) != str:
        raise ValueError
    
    return str(int(num1) * int(num2))


x = multiply("1", "2")
print(x)