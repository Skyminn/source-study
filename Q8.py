#연습문제 8-1
def sel_sort(a):
     n=len(a)
     for i in range(0,n-1):
         min_idx=i
         for j in range(i+1,n):
             if a[j]<a[min_idx]:
                 min_idx = j
         a[i], a[min_idx] = a[min_idx], a[i]
d=[2,4,5,1,3]
sel_sort(d)
print(d)

#연습문제 8-2
def sel_sort2(a):
    n=len(a)
    for i in range(0,n-1):
        max_idx=i
        for j in range(i+1,n):
            if a[j]>a[max_idx]:
                max_idx=j
        a[i], a[max_idx] = a[max_idx], a[i]
d=[2,4,5,1,3]
sel_sort2(d)
print(d)