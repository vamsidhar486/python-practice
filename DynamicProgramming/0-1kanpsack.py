"""
0-1 KNAPSACK sample problem
"""


def max_profit(weight, profit, bag, n):
    """
    using recursion for intuition
    :param weight:
    :param profit:
    :param bag:
    :param n:
    :return: maximum profit
    """
    if bag == 0 or n == 0:
        return 0
    if weight[n] > bag:
        return max_profit(weight, profit, bag, n - 1)
    else:
        return max(max_profit(weight, profit, bag, n - 1),
                   profit[n] + max_profit(weight, profit, bag - weight[n], n - 1))


def max_profit(weight, profit, bag, n):
    """
    DP with memoization
    :param weight:
    :param profit:
    :param bag:
    :param n:
    :return:
    """

    if bag == 0 or n == 0:
        return 0

    if mem[w][n] != -1:
        return mem[w][n]

    if weight[n] > bag :
        return max_profit(weight, profit, bag, n-1)
    else:
        result = max(max_profit(weight, profit, bag, n-1),
                     profit + max_profit(weight, profit, weight - weight[n], n-1))
    mem[bag][n] = result

    return mem[bag][n]

def max_profit(weight, profit, bag, n):
    """
    DP with tabulation
    :param weight:
    :param profit:
    :param bag:
    :param n:
    :return:
    """


weight = [2, 3, 5]
profit = [7, 9, 10]
bag = 10

print(max_profit(weight, profit, bag, len(weight) - 1))
