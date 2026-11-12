
def count_occurrences(target, values):
    # Part 1: Recursion
    if len(values) == 0:
        return 0

    count = 1 if values[0] == target else 0
    return count + count_occurrences(target, values[1:])


def is_sorted(values):
    # Part 2: Recursion
    if len(values) <= 1:
        return True

    if values[0] <= values[1]:
        return is_sorted(values[1:])
    else:
        return False


class Rectangle:
    def __init__(self, width, height):
        # Part 3: OOP
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.width}x{self.height}"


class Square(Rectangle):
    # Part 4: Inheritance
    def __init__(self, side):
        super().__init__(side, side)


def main():
    # Test Part 1
    print(count_occurrences(2, [1, 2, 2, 3, 2]))
    print(count_occurrences(5, [1, 2, 3]))

    # Test Part 2
    print(is_sorted([1, 2, 3]))
    print(is_sorted([2, 2, 3]))
    print(is_sorted([1, 3, 2]))

    # Test Part 3
    r = Rectangle(3, 4)
    print(r.area())
    print(r.perimeter())
    print(r)

    # Test Part 4
    s = Square(5)
    print(s.area())
    print(s.perimeter())
    print(s)


if __name__ == "__main__":
    main()
