#예제 4-1
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

print(fact(1))
print(fact(5))
print(fact(10))

#예제 4-2
def fact_2(n):
    if n<=1:
        return 1
    return n*fact_2(n-1)

print(fact_2(1))
print(fact_2(5))
print(fact_2(10))

#연습문제 4-1
def sum(n):
    if n<1:
        return 0
    return n+sum(n-1)

print(sum(10))

#연습문제 4-2
def find_max(a,n):
    if n==1:
        return a[0]
    max=find_max(a,n-1)
    if max>a[n-1]:
        return max
    else:
        return a[n-1]

v=[17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v,len(v)))