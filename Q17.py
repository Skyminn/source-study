#가짜동전을 찾는 알고리즘1
#주어진 동전 n개 중에 가짜 동전(fake)을 찾아내는 알고리즘
#입력: 전체 동전 위치의 시작과 끝(0, n-1)
#출력: 가짜 동전의 위치 번호

#무게재기 함수
#a에서 b까지에 놓인 동전과
#c에서 d까지에 놓인 동전의 무게를 비교
#a에서 b까지에 가짜 동전이 있으면(가벼우면): -1
#c에서 d까지에 가짜 동전이 있으면(가벼우면): 1
#가짜 동전이 없으면(양쪽 무게가 같으면): 0


def weigh(a, b, c, d):
    fake = 29 #가짜 동전의 위치(알고리즘은 weigh() 함수를 이용하여 이 값을 맞혀야 함)
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    
    return 0

    #weigh() 함수(저울질)을 이용하여
    # left에서 right까지에 놓인 가짜 동전의 위치를 찾아냄

def find_fakecoin(left, right):
    for i in range(left + 1, right + 1):
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i 
    return -1

n = 100
print(find_fakecoin(0, n-1)) 




#주어진 동전 n개 중에 가짜 동전(fake)을 찾아내는 알고리즘2

def weigh_2(a, b, c, d):
    fake = 29
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

def find_fakecoin_2(left, right):
    if left == right:
        return left
    #left에서 right까지에 놓인 동전을 두 그룹(g1_left~g1_right, g2_left~g2_right)으로 나눔
    #동전 수가 홀수면 두 그룹으로 나누고 한 개가 남음
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1

    result = weigh_2(g1_left, g1_right, g2_left, g2_right)
    if result == -1:
        return find_fakecoin_2(g1_left, g1_right)
    elif result == 1:
        return find_fakecoin_2(g2_left, g2_right)
    else: 
        return right

n = 100
print(find_fakecoin_2(0, n-1))