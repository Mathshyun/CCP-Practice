def integrals(a, b, n):
    s = 0
    for i in range(n):
        x = a + (b - a) * i / n
        s += (x ** 5 - x ** 4) * (b - a) / n
    return s

def test_integrals():
    (a, b) = (0, 10)
    testcase = [10, 100, 1000, 10000, 100000]
    for i in testcase:
        r = integrals(a, b, i)
        print('Sum of %6d rectangle(s) of int (x^5-x^4) dx from %f to %f is %f' % (i, a, b, r))

def est_pi(n):
    from random import random
    cir = 0
    for i in range(n):
        (x, y) = (random(), random())
        if (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25: cir += 1
    return 4 * cir / n

def test_est_pi():
    testcase = [10, 100, 1000, 10000, 100000]
    for i in testcase:
        r = est_pi(i)
        print('Estimated pi value of %6d case(s) is %f' % (i, r))

if __name__ == '__main__':
    test_integrals()
    print()
    test_est_pi()
