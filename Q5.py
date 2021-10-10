#예제 5-1
def gcd(a,b):
    i=min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i-=1

print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))

#예제 5-2
def gcd_2(a,b):
    if b==0:
        return a
    return gcd_2(b,a%b)

print(gcd_2(1,5))
print(gcd_2(3,6))
print(gcd_2(60,24))
print(gcd_2(81,27))

#연습문제 5-1
def fibo_sequence(n):
    if n<=1:
        return n
    return fibo_sequence(n-2)+fibo_sequence(n-1)

print(fibo_sequence(7))