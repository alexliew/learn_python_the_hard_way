i = 0
numbers = []

while i < 6:
    print("At the top i is {:d}".format(i))
    numbers.append(i)

    i += 1
    print("Numbers now:", numbers)
    # using string formatting you can get the same result
    # print("Numbers now: {!s}".format(numbers))
    print("At the bottom i is {:d}".format(i))

print("The numbers: ")

for num in numbers:
    print(num)


def foo(n, inc):
    i = 0
    numbers = []
    while i < n:
        print("At the top i is {:d}".format(i))
        numbers.append(i)

        i += inc
        print("Numbers now:", numbers)
        # using string formatting you can get the same result
        # print("Numbers now: {!s}".format(numbers))
        print("At the bottom i is {:d}".format(i))

def bar(n, inc):
    numbers = []
    for i in range(0, n, inc):
        print("At the top i is {:d}".format(i))
        numbers.append(i)

        print("Numbers now:", numbers)
        # using string formatting you can get the same result
        # print("Numbers now: {!s}".format(numbers))
        print("At the bottom i is {:d}".format(i))
