import math


def fun():
    print("Hi from fun")
    s = "Hey this is great"
    s.count("e")
    s = s.replace("great", "awesome")
    print(s)
    sentence = "This is a coffee cup, you can also pour water in it"
    sentence = sentence.replace("coffee", "tea", 1)
    print("no" in sentence)
    print(sentence)
    l = ["This", "is", "1", "of", "the", "best", "features"]
    l.append("moo")
    l[0] = "That"
    listSen = ""
    for i in range(len(l)):
        listSen += l[i] + " "
    print(listSen)
    sqrt = math.sqrt(16)
    fac4 = math.factorial(4)
    print(f"sqrt: {sqrt}")
    print(fac4)


def modulo(x, y):
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
    rem = modulo(60, 9)
    print(rem)


if __name__ == "__main__":
    main()
