import time
from collections import deque
from random import choice, randint

def first_unique_char(s):

    h_map = {}
    for i in range(len(s)):
        if s[i] in h_map:
            h_map[s[i]] += 1
        else:
            h_map[s[i]] = 1

    for i in range(len(s)):
        if h_map[s[i]] == 1:
            return i

    return -1

def first_unique_test(s):
    stack = deque()
    h_map = {}

    for i in range(len(s)):
        if s[i] in h_map:
            h_map[s[i]] += 1
            while stack and h_map[stack[0][0]] > 1:
                stack.popleft()
        else:
            h_map[s[i]] = 1
            stack.append((s[i], i))

    if stack:
        return stack[0][1]

    return -1

def first_unique_test_2(s):
    h_map = {}
    dup_map = {}
    
    for i in range(len(s)):
        if s[i] in h_map:
            h_map.pop(s[i], None)
            dup_map[s[i]] = 0

        elif s[i] not in dup_map:
            h_map[s[i]] = i

    if h_map:
        return min(h_map.values())

    return -1

if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join([choice(chars) for x in range(10**5)])
    random_index = choice(range(len(s)))

    s = s[:random_index] + "@" + s[random_index + 1:]

    start = time.time()
    print(first_unique_char(s))
    print(f"Original: {time.time() - start}\n")

    start = time.time()
    print(first_unique_test(s))
    print(f"Test: {time.time() - start}\n")

    start = time.time()
    print(first_unique_test_2(s))
    print(f"Test 2: {time.time() - start}")

    print(randint(0, 1000))