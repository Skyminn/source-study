#1부터 n까지의 합 구하기
#예제1-1
def sum(n):
    s=0
    for i in range (1,n+1):
        s+=i
    return s
print(sum(10))
print(sum(100))

#예제1-2
def sum_2(n):
    return n*(n+1)//2
print(sum_2(10))
print(sum_2(100))

#연습문제 1-1
def sum_3(n):
    s=0
    for i in range(1,n+1):
        s=s+pow(i,2)
    return s
print(sum_3(10))
#연습문제 1-2 :O(n)
#연습문제 1-3: O(1)