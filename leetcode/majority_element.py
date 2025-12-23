def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 1
    k = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == k:
            count += 1
        else:
            count -= 1
            if count == 0:
                count += 1
                k = nums[i]
    return k
