def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    [7, 1, 5, 3, 6, 4]
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if buy > prices[i]:
            buy = prices[i]
        else:
            temp_profit = prices[i] - buy
            if temp_profit > profit:
                profit = temp_profit

    return profit
