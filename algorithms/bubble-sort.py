def bubbleSort(nums: list) -> list:
    """
    Bubble sort algorithm.

    :param nums: List of integers to be sorted
    :type nums: list
    :return: Sorted list of integers
    :rtype: list
    """
    """
    This algorithm takes a list as an input
    it starts comparing the first element with next element
    then if the element next to it is smaller than the current element it is swapped and 
    the process is repeated and the last element will be the largest element
    and then the range decreases as list is sorted"""

    for i in range(0, len(nums) - 1):
        swapped = False

        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums
