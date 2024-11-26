def bubble_sort(a):
    n = len(a)
    unordered = True
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                unordered = True
        n -= 1
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i - 1
        while j >= 0 and a[j] > tmp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp
    return a


def selection_sort(a):
    for i in range(len(a)-1):
        imin = i
        for j in range(i+1, len(a)):
            if a[j] < a[imin]:
                imin = j
        a[i], a[imin] = a[imin], a[i]
    return a

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        elem = lst[0]
        left = []
        medium = []
        right = []
        for i in lst:
            if i < elem:
                left.append(i)
            elif i > elem:
                right.append(i)
            else:
                medium.append(i)
        a = quick_sort(left)
        b = quick_sort(right)
        return a + medium + b
