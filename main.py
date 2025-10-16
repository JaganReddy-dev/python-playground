import math


def fun():
    # This is fun with python
    print("Hi from fun")
    s = "Hey this is great"
    s.count("e")
    s = s.replace("great", "awesome")
    print(s)
    # this is playing with strings
    sentence = "This is a coffee cup, you can also pour water in it"
    sentence = sentence.replace("coffee", "tea", 1)
    print("no" in sentence)
    print(sentence)
    # understanding lists(note: it can contain objects of different types )
    let = ["This", "is", "1", "of", "the", "best", "features"]
    newList = [3.5, None, 3.5, True, "hello"]
    print(f"hey from newList slice: {newList[2:4]}")
    let.append("moo")
    let[0] = "That"
    listNone = [None]
    k = [1, True, "String Here!"]
    k.append(7.6)
    k.append(2 + 3j)
    print(k)
    names = ["Jane", "Adam", "Ryan", "Bob", "Zordon", "Jack", "Jackenzie"]
    names.sort()
    print(names)

    listSen = ""

    for i in range(len(let)):
        listSen += let[i] + " "
    print(listSen)
    # examples with math module
    sqrt = math.sqrt(16)
    fac4 = math.factorial(4)
    print(f"sqrt: {sqrt}")
    print(fac4)
    # decimal comparision using math.isclose()
    deciimalCompare = math.isclose((0.1 + 0.2 + 0.1), 0.6)
    print(f"decimal comparision: {deciimalCompare}")
    # understanding arithmetics and return data types
    print(5 / 3)
    print(1.5**2)
    print(type(1.5**2))
    # checking if two variables are qual using is
    x = 1.2
    y = 1.2
    print(f"is: {x is y}")
    # string manipulation
    center = "cat".center(11, "-")
    print(center)
    newString = "I.am.aware.that.spaces.are.a.thing"
    print(newString.replace(".", " ", 3))
    term = "  basket    "
    print(len(term.strip(" ")))
    print("Hello\n\tover there")


# methods to check type of object type()=> returns type of data, validatiing data type isinstance(value, dataType)=> return true or false
# understanding user defined functions using remainder function
def reminder(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    if x < 0 or y < 0:
        raise ValueError("Only positive integers supported")

    while x >= y:
        x -= y
    return x


def main():
    print("Hello from python-projects!")
    fun()
    rem = reminder(60, 9)
    print(rem)


if __name__ == "__main__":
    main()
