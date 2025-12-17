some_list = [1, 2, 3, 4, 5]


def func_with_args_and_kwargs(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)
    total = sum(args) + sum(kwargs.values())
    return total


def mean(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0


result = func_with_args_and_kwargs(10, 20, a=1, b=2)
print("Result:", result)
