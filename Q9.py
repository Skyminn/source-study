#연습문제 9-1

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)

#연습문제 9-2

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j>=0 and a[j] < key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)