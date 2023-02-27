

def add_binary(a: str, b: str):
    if a == "0":
        return b

    elif b == '0':
        return a

    elif a == "0" and b == '0':
        return '0'
    
    total = 0

    for numbers in [a,b]: 
        mul = 1
        num = 0
        for i in numbers[::-1]:
            if i == "1":
                num += int(i) * mul
            mul *= 2
        total += num
    print(total)
    bn = ["0"] * total
    i = 0

    while total > 0:
        bn[i] = str(int(total) % 2)
        total = int(total / 2)
        i += 1

    return str(int("".join(bn[::-1])))

a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"
print(add_binary(a, b))



