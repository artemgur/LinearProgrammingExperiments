def profit(a):
    avg_profit1 = ((80 * 100 - 35 * a) + 45 * a) / 2
    p_profit1 = (a - 100) / 200
    avg_profit2 = 45 * a
    p_profit2 = (300 - a) / 200

    local_profit = avg_profit1 * p_profit1 + avg_profit2 * p_profit2

    return local_profit





max_a = -1
max_profit = -1

for a in range(100, 300 + 1):
    local_profit = profit(a)
    if local_profit > max_profit:
        max_profit = local_profit
        max_a = a

print(max_a)
print(max_profit)