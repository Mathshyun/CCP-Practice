def f1(ls):
    if not ls:
        return 0
    return ls[0] + f1(ls[1:])

def f2(n):
    if n == 1:
        return 1
    elif n % 2:
        return f2(3 * n + 1) + 1
    else:
        return f2(n // 2) + 1

def f3(ls):
    if not ls:
        return None
    print(ls[-1])
    f3(ls[:-1])

def f4(ls):
    if not ls:
        return None
    if ls[0] % 2:
        print(ls[0] * 3)
    f4(ls[1:])

def f5(ls):
    if not ls:
        return None
    if ls[-1] % 2:
        print(ls[-1] * 3)
    else:
        print(ls[-1])
    f5(ls[:-1])

def f6(ls):
    r = []
    for i in ls:
        if type(i) == list:
            i = f6(i)
            for j in i:
                r.append(j)
        else:
            r.append(i)
    return r

def f7(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return f7(n - 1) + f7(n - 2)

def f8(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return f8(s[1:-1])
    else:
        return False

def f9(n):
    if n == 0:
        return 1
    else:
        return n * f9(n - 1)

def f10(ls):
    if not ls:
        return 0
    else:
        return 1 + f10(ls[1:])

def f11(ls):
    if not ls:
        return None
    if len(ls) == 1:
        return ls[0]
    else:
        return f11(ls[1:])

def f12(n):
    if n < 1:
        return None
    print(n)
    if n > 1:
        f12(n - 1)

def f13(n):
    if n < 10:
        return 1
    else:
        return f13(n // 10) + 1

def f14(ls):
    if not ls:
        return None
    if ls[0] % 2:
        return ls[0]
    else:
        return f14(ls[1:])

def f15(ls):
    if not ls:
        return 0
    if ls[0] % 2:
        return ls[0] + f15(ls[1:])
    else:
        return f15(ls[1:])

def f16(ls):
    if not ls:
        return []
    if ls[0] % 2:
        return [ls[0]] + f16(ls[1:])
    else:
        return f16(ls[1:])

def f17(ls):
    if len(ls) == 2:
        return ls[0]
    else:
        return f17(ls[1:])

def f18(a, b):
    if a < b:
        return f18(b, a)
    elif b == 0:
        return a
    else:
        return f18(b, a % b)

def f19(ls1, ls2):
    if ls1 == ls2 == []:
        return []
    elif ls1 == []:
        return ls2
    elif ls2 == []:
        return ls1
    elif ls1[0] < ls2[0]:
        return [ls1[0]] + f19(ls1[1:], ls2)
    else:
        return [ls2[0]] + f19(ls1, ls2[1:])

def f20(ls):
    if len(ls) <= 1:
        return ls
    return f19(f20(ls[:len(ls) // 2]), f20(ls[len(ls) // 2:]))
