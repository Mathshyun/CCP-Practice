'''
Sorting Comparison Project
SNU CCP
Code written by Hyun
'''

import copy
import random
import sys
import time

def selection_sort(data):
    global cnt
    l = len(data)
    r = []
    for i in range(l, 0, -1):
        min = data[0]
        for j in data[1:]:
            cnt += 1
            if j < min: min = j
        data.remove(min)
        r.append(min)
    return r

def insertion_sort(data):
    global cnt
    for i in range(1, len(data)):
        for j in range(i - 1, 0, -1):
            cnt += 1
            if data[j] < data[j - 1]:
                data[j - 1], data[j] = data[j], data[j - 1]
    return data

def bubble_sort(data):
    global cnt
    for i in range(len(data) - 1):
        for j in range(i):
            cnt += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def merge(data1, data2):
    global cnt
    if data1 == data2 == []:
        return []
    if data1 == []:
        return data2
    if data2 == []:
        return data1
    cnt += 1
    if data1[0] < data2[0]:
        return [data1[0]] + merge(data1[1:], data2)
    else:
        return [data2[0]] + merge(data2, data1[1:])

def merge_sort(data):
    global cnt
    l = len(data)
    if l <= 1: return data
    m = l // 2
    return merge(merge_sort(data[:m]), merge_sort(data[m:]))

def quick_sort(data):
    global cnt
    l = len(data)
    if l <= 1: return data
    piv = data[l // 2]
    ls1, ls2 = [], []
    data.remove(piv)
    for i in data:
        cnt += 1
        if i < piv:
            ls1.append(i)
        else:
            ls2.append(i)
    return quick_sort(ls1) + [piv] + quick_sort(ls2)

def test_selection_sort(data, file):
    global cnt
    n = len(data)
    cnt = 0
    sTime = time.time()
    data = selection_sort(data)
    fTime = time.time()
    print('For selection sort of %d elements:' % n)
    print('%0.16f seconds elapsed' % (fTime - sTime))
    print('%d times of comparison operation executed' % cnt)
    print()
    file.write('For selection sort of %d elements:\n' % n)
    file.write('%0.16f seconds elapsed\n' % (fTime - sTime))
    file.write('%d times of comparison operation executed\n' % cnt)
    file.write('\n')

def test_insertion_sort(data, file):
    global cnt
    n = len(data)
    cnt = 0
    sTime = time.time()
    data = insertion_sort(data)
    fTime = time.time()
    print('For insertion sort of %d elements:' % n)
    print('%0.16f seconds elapsed' % (fTime - sTime))
    print('%d times of comparison operation executed' % cnt)
    print()
    file.write('For insertion sort of %d elements:\n' % n)
    file.write('%0.16f seconds elapsed\n' % (fTime - sTime))
    file.write('%d times of comparison operation executed\n' % cnt)
    file.write('\n')

def test_bubble_sort(data, file):
    global cnt
    n = len(data)
    cnt = 0
    sTime = time.time()
    data = bubble_sort(data)
    fTime = time.time()
    print('For bubble sort of %d elements:' % n)
    print('%0.16f seconds elapsed' % (fTime - sTime))
    print('%d times of comparison operation executed' % cnt)
    print()
    file.write('For bubble sort of %d elements:\n' % n)
    file.write('%0.16f seconds elapsed\n' % (fTime - sTime))
    file.write('%d times of comparison operation executed\n' % cnt)
    file.write('\n')

def test_merge_sort(data, file):
    global cnt
    n = len(data)
    cnt = 0
    sTime = time.time()
    data = merge_sort(data)
    fTime = time.time()
    print('For merge sort of %d elements:' % n)
    print('%0.16f seconds elapsed' % (fTime - sTime))
    print('%d times of comparison operation executed' % cnt)
    print()
    file.write('For merge sort of %d elements:\n' % n)
    file.write('%0.16f seconds elapsed\n' % (fTime - sTime))
    file.write('%d times of comparison operation executed\n' % cnt)
    file.write('\n')

def test_quick_sort(data, file):
    global cnt
    n = len(data)
    cnt = 0
    sTime = time.time()
    data = quick_sort(data)
    fTime = time.time()
    print('For quick sort of %d elements:' % n)
    print('%0.16f seconds elapsed' % (fTime - sTime))
    print('%d times of comparison operation executed' % cnt)
    print()
    file.write('For quick sort of %d elements:\n' % n)
    file.write('%0.16f seconds elapsed\n' % (fTime - sTime))
    file.write('%d times of comparison operation executed\n' % cnt)
    file.write('\n')

def test_builtin_sort(data, file):
    n = len(data)
    sTime = time.time()
    data = sorted(data)
    fTime = time.time()
    print('For builtin sort of %d elements:' % n)
    print('%0.16f seconds elapsed' % (fTime - sTime))
    print()
    file.write('For builtin sort of %d elements:\n' % n)
    file.write('%0.16f seconds elapsed\n' % (fTime - sTime))
    file.write('\n')

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)

    tcFile = open('sorting_comparison_test_case.txt', 'w')
    rsFile = open('sorting_comparison_result.txt', 'w')

    n = 100
    data = list(range(n))
    random.shuffle(data)
    tcFile.write('The following test case used for sorting %d elements:\n%s\n\n' % (n, data))
    test_selection_sort(copy.copy(data), rsFile)
    test_insertion_sort(copy.copy(data), rsFile)
    test_bubble_sort(copy.copy(data), rsFile)
    test_merge_sort(copy.copy(data), rsFile)
    test_quick_sort(copy.copy(data), rsFile)
    test_builtin_sort(copy.copy(data), rsFile)
    print()
    rsFile.write('\n')

    n = 1000
    data = list(range(n))
    random.shuffle(data)
    tcFile.write('The following test case used for sorting %d elements:\n%s\n\n' % (n, data))
    test_selection_sort(copy.copy(data), rsFile)
    test_insertion_sort(copy.copy(data), rsFile)
    test_bubble_sort(copy.copy(data), rsFile)
    test_merge_sort(copy.copy(data), rsFile)
    test_quick_sort(copy.copy(data), rsFile)
    test_builtin_sort(copy.copy(data), rsFile)
    print()
    rsFile.write('\n')

    n = 10000
    data = list(range(n))
    random.shuffle(data)
    tcFile.write('The following test case used for sorting %d elements:\n%s\n\n' % (n, data))
    test_selection_sort(copy.copy(data), rsFile)
    test_insertion_sort(copy.copy(data), rsFile)
    test_bubble_sort(copy.copy(data), rsFile)
    test_merge_sort(copy.copy(data), rsFile)
    test_quick_sort(copy.copy(data), rsFile)
    test_builtin_sort(copy.copy(data), rsFile)
    print()
    rsFile.write('\n')

    print('The test case file has been generated.')

    tcFile.close()
    rsFile.close()
