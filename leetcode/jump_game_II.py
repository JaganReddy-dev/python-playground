def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    currRange = 0
    jumps = 0
    currFarthest = 0

    for i in range(len(nums) - 1):
        currFarthest = max(currFarthest, i + nums[i])
        if i == currRange:
            currRange = currFarthest
            jumps += 1

    return jumps
