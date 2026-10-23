def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

        if price < min_price:
            min_price = price

    return max_profit


prices = list(map(int, input("Enter stock prices: ").split()))
print(max_profit(prices))