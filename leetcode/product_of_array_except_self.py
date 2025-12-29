def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    idx = -1
    zeros = 0
    product = 1

    n = len(nums)

    for i in range(n):
        if nums[i] == 0:
            zeros += 1
            idx = i
        else:
            product *= nums[i]

    res = [0] * n

    if zeros == 0:
        for i in range(n):
            res[i] = product // nums[i]
    elif zeros == 1:
        res[idx] = product

    return res

    # result = [0] * n
    # suffixList = [1] * n
    # prefixList = [1] * n

    # for i in range(i, n):
    #     prefixList[i] = nums[i - 1] * prefixList[i - 1]
    # for i in range(n - 2, -1, -1):
    #     suffixList[i] = nums[i + 1] * suffixList[i + 1]

    # for i in range(n):
    #     result[i] = prefixList[i] * suffixList[i]

    # return result
