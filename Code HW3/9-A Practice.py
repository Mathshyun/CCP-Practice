def f1(ls):
    return len(list(filter(lambda x: x % 2, ls)))

def f2(ls):
    any(map(print, filter(lambda x: x % 2, ls)))

def f3(ls):
    return sum(filter(lambda x: x % 2, ls))

def f4(ls):
    return sum(filter(lambda x: ls[x] % 2, range(len(ls))))

def f5(ls):
    return list(map(lambda x: x ** 2, ls))

def f6(ls):
    return max(ls)

def f7(ls):
    return sum(ls) / len(ls)

def f8(a, b, n):
    any(map(print, filter(lambda x: not x % n, range(a, b + 1))))

def f9(w, h):
    any(map(print, ['*' * w] * h))

def f10(n):
    any(map(print, ['*' * x for x in range(1, n + 1)]))

def f11(ls):
    return ls == sorted(ls, reverse=True)

def f12(ls):
    return all(map(lambda x: x < 0, ls))

def f13(ls, target):
    return max(filter(lambda x: ls[x] == target, range(len(ls))))

def f14(ls):
    return max(filter(lambda x: ls[x] < 0, range(len(ls))))

def f15(ls):
    return sum(map(lambda x: ls[x], range(0, len(ls), 2)))

def f16(n):
    any(map(print, ['*' * x for x in range(n, 0, -1)]))

def f17(ls):
    any(map(print, [ls[x] for x in range(len(ls) - 1, -1, -2)]))

def f18(n):
    return f18(n - 1) * n if n > 0 else 1

def f19(mtx):
    any(map(print, map(sum, mtx)))

def f20(mtx):
    any(map(print, [mtx[x][x] for x in range(len(mtx))]))

def f21(ls):
    any(map(print, map(f18, ls)))

def f22(ls):
    any(map(print, [' '.join(map(str, range(num, -1, -1))) for num in ls]))

def f23(ls1, ls2):
    return list(map(lambda x, y: x + y, ls1, ls2))

def f24(n):
    any(map(print, filter(lambda x: not(x % 2 and x % 3), range(1, n + 1))))

def f25(ls):
    return max(x for y in ls for x in y)

def f26(ls):
    return sorted(ls)[-2]

def f27(n):
    return int(str(n)[0])

def f28(ls):
    any(map(print, map(max, ls)))
