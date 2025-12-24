def canJump(nums):
    length = len(nums)
    maxIndex = 0
    for i in range(length):
        if i > maxIndex:
            return False
        maxIndex = max(maxIndex, i + nums[i])
    return True
