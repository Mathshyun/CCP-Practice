def f_rec1(tree):
    if not tree:
        return 0
    lsub, rsub = f_rec1(tree[1]), f_rec1(tree[2])
    if lsub >= rsub:
        return lsub + 1
    else:
        return rsub + 1

def f_rec2(tree):
    if not tree:
        return 0
    return f_rec2(tree[1]) + f_rec2(tree[2]) + 1

def f_rec3(tree):
    if not tree:
        return 0
    return tree[0] + f_rec3(tree[1]) + f_rec3(tree[2])

def f_rec4(tree):
    if not tree:
        return
    f_rec4(tree[1])
    print(tree[0])
    f_rec4(tree[2])

def f_rec5(tree):
    if not tree:
        return -1
    if not tree[1]:
        return tree[0]
    return f_rec5(tree[1])
