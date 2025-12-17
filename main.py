def main():
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    exp = (index for index, value in enumerate(values) if value % 2 == 0)
    print(list(exp))  # Output: [1, 3, 5, 7, 9]


if __name__ == "__main__":
    main()
