def selectionSort(nums: list) -> list:
    """
    Selection sort algorithm.

    :param nums: List of integers to be sorted
    :type nums: list
    :return: Sorted list of integers
    :rtype: list
    """

    n = len(nums)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums
