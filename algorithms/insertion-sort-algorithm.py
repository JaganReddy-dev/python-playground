def insertionSort(nums: list) -> list:
    """
    Docstring for insertionSort

    :param nums: Description
    :type nums: list
    :return: Description
    :rtype: list
    """
    """
    This algorithm sorts the given list by comparing the current element with the previous element and then if the current 
    element is lesser than the previous element,it keeps the element in temp and increase the 
    prefix of the list and then check if temp is greater than the previous element and places the element in the correct position.
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[i] > nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


print(insertionSort([5, 4, 3, 2, 1]))
