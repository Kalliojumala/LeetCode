
def twoSum(nums: list, target: int) -> list:
    tbl = {}
    for index, value in enumerate(nums):
        trg = target - value
        if trg in tbl:
            return sorted([index, tbl[trg]])
        else:
            tbl[value] = index




arr = [2,7,11,15]


t = 9

print(twoSum(arr, t))
