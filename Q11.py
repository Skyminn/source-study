#거품 정렬

def bubble_sort(a):
    n = len(a)
    while True:
        Flag = False
        for i in range(0, n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                Flag = True
        if Flag == False:
            return

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
    