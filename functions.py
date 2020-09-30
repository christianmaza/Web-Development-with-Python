def square(x):
    return x * x


def main():
    for i in range(5):
        # .format is the older way for placing data in placeholders.
        print("{} squared is {}".format(i, square(i)))
        # the newest way is to use print(f"{i}...{square(i)")


if __name__ == "__main__":
    main()
