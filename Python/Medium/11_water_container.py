"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:

n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4
"""

#surface of container =  min(i, j)  * abs(i-j)
def solution_brute(arr: list):
    #SLOOOOOOOOOOOOOOOW...
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            max_height = min(arr[i], arr[j])
            dist = abs(i-j)
            result = max(result, max_height * dist)

    return result


def solution(height: list):
    
    pointer = 0
    pointer_2 = len(height) - 1
    result = min(height[pointer], height[pointer_2]) * (pointer_2 - pointer)
    
    while pointer < pointer_2:
        if height[pointer] <= height[pointer_2]:
            pointer += 1
        else:
            pointer_2 -= 1
        
        result = max(result, min(height[pointer], height[pointer_2]) * (pointer_2 - pointer))

    return result

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(solution(height))