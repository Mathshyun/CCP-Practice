# Advanced Practice - Function (1): Searching
def first_perfect_square(numbers):
    for i in range(len(numbers)):
        if numbers[i] >= 0:
            rt = numbers[i] ** 0.5
            if round(rt) == rt:
                return i
    return -1

if __name__ == "__main__":
    print(
        first_perfect_square(list(range(5))),
        first_perfect_square([2, 4, 6, 8, 10, 12]),
        first_perfect_square([6, 8, 10, 12, 9]),
        first_perfect_square([1,1]),
        first_perfect_square([-6, 6, -2, 2, -3, 3]),
        first_perfect_square([42]),
        first_perfect_square([]),
        first_perfect_square([123456789123456789**2])
    )

# Advanced Practice - Function (2): Counting
def num_perfect_squares(numbers):
    cnt = 0
    for i in numbers:
        if i >= 0:
            rt = i ** 0.5
            if round(rt) == rt:
                cnt += 1
    return cnt

if __name__ == "__main__":
    print(
        num_perfect_squares([]),
        num_perfect_squares([0]),
        num_perfect_squares([0,1]),
        num_perfect_squares(list(range(10))),
        num_perfect_squares([3]*10),
        num_perfect_squares([4]*10),
        num_perfect_squares([-4, -2, 0, 2, 4])
    )

# Advanced Practice - Function (3): Second Largest Element
def second_largest(values):
    mx1, mx2 = (values[0], values[1]) if values[0] >= values[1] else (values[1], values[0])
    for i in values[2:]:
        if i > mx2:
            if i > mx1:
                mx1, mx2 = (i, mx1)
            else:
                mx2 = i
    return mx2

if __name__ == "__main__":
    print(
        second_largest([3, -2, 10, -1, 5]),
        second_largest([-2, 1, 1, -3, 5]),
        second_largest([1,2,3,3]),
        second_largest(["alpha", "gamma", "beta", "delta"]),
        second_largest([3.1, 3.1]),
        second_largest([True, False, False, True]),
        second_largest([False, False, True])
    )
