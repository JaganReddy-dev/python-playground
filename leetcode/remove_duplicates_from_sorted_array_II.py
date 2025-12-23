def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    1, 1, 1, 2, 2, 2, 3, 4, 4
    k = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k
