def count_vowels(letters):
    return sum(1 for letter in letters if letter in "aeiouAEIOU")


gen = [(n, n + 2) for n in range(2, 8) if n != 3]

[("hello", ind + 1) for _, ind in enumerate(range(100))]

sum(i for i in range(1, 101, 2))

[[1 for _ in range(3)] for _ in range(4)]

print(["hello" if i % 2 == 0 else "goodbye" for i in range(10)])

print([1 if i.lower() == "o" else 0 for i in "Hello. How Are You?" if i not in " .?"])


def count_even(nums):
    return sum(1 for num in nums if num % 2 == 0)


new_str = "3.2,2.4,99.8"
print(tuple(float(num) for num in new_str.split(",")))
print(new_str.split(","))
