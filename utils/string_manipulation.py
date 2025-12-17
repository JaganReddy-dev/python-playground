def string_manipulation(str_obj: str) -> list:
    """
    Docstring for string_manipulation function.

    :param str_obj: Accepts a string object
    :type str_obj: str
    :return: List containing length, replaced string, parts, and space count
    :rtype: list
    """
    length = len(str_obj)
    replace = str_obj.replace(" ", "-")
    parts = str_obj.split(" ")
    space_count = str_obj.count(" ")
    return [length, replace, parts, space_count]


center = "cat".center(11, "-")
print(center)
newString = "I.am.aware.that.spaces.are.a.thing"
print(newString.replace(".", " ", 3))
term = "  basket    "
print(len(term.strip(" ")))
print("Hello\n\over there")

# methods to check type of object type()=> returns type of data, validatiing data type isinstance(value, dataType)=> return true or false
