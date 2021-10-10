#예제2-1
def find_max(a):
    n=len(a)
    max=a[0]
    for i in range(1,n):
        if a[i]>max:
            max=a[i]
    return max

v=[17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))

#예제2-2
def find_index(a):
    n=len(a)
    max_index=0
    for i in range(1,n):
        if a[i]>a[max_index]:
            max_index=i
    return max_index
v=[17, 92, 18, 33, 58, 7, 33, 42]
print(find_index(v))

#연습문제 2-1
def find_min(a):
    n=len(a)
    min=a[0]
    for i in range(1,n):
        if a[i]<a[0]:
            min=a[i]
    return min
v=[17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))