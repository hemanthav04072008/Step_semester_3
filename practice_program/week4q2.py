def maxprofit(prices):
    minimumprofit = prices[0]
    maximumprofit = 0

    for price in prices:
        if price < minimumprofit:
            minimumprofit = price

        profit = price - minimumprofit
        if profit > maximumprofit:
            maximumprofit = profit

    return maximumprofit


prices = [7, 1, 2, 3, 5, 6, 7]
print(maxprofit(prices))