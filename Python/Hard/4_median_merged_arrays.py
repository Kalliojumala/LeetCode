#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

def solution(arr, arr_2):

    from collections import deque
    arr = deque(arr)
    arr_2 = deque(arr_2)
    result_arr = deque([])

    result_len = (len(arr) + len(arr_2)) #len of result array if fully merged
    req_len = result_len // 2 + 1 #only iterate the arrays to halfway point + 1

    while len(result_arr) < req_len:
        val1 = arr[0] if len(arr)!=0 else 0                 #min value for both arrays is 1, if arr is empty value 0 makes sure 
        val2 = arr_2[0] if len(arr_2)!=0 else 10**6 + 10    #second array is cleared as well, 10**6 + 10 for empty arr_2 does the same for arr
        if val1 <= val2 and len(arr) != 0:      
            result_arr.append(arr.popleft())    #pick from arr if arr[0] smaller and not empty 
        else:
            result_arr.append(arr_2.popleft()) 

    if result_len % 2 == 0:
        return float((result_arr[-1] + result_arr[-2]) / 2)

    return float(result_arr[-1])

if __name__ == '__main__':
    nums1 = [1] # [1,2,3,3,4,5]
    nums2 = []
    print(solution(nums1, nums2))

    nums1 = [1,2]
    nums2 = [3,4]
    print(solution(nums1, nums2))