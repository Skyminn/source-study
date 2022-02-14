#최대 수익을 구하는 알고리즘1
#주어진 주식 가격을 보고 얻을 수 있는 최대 수익을 구하는 알고리즘
# 출력: 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 값
def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    
    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))



#최대수익을 구하는 알고리즘2
def max_profit2(prices):
    n = len(prices)
    max_profit2 = 0
    min_price = prices[0]
    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit2:
            max_profit2 = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit2
stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
