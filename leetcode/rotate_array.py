def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n

    def reverse(left, right, lsit_nums):
        while left < right:
            lsit_nums[left], lsit_nums[right] = lsit_nums[right], lsit_nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1, nums)
    reverse(0, k - 1, nums)
    reverse(k, n - 1, nums)
