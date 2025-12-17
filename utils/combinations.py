from itertools import combinations


fruits = ["apples", "bananas", "pears", "pears", "oranges"]
print(
    list(combinations(fruits, 2)).count(("pears", "oranges"))
    / len(list(combinations(fruits, 2)))
)
