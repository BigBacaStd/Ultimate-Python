def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

sum_with_range(1, 10)
sum_with_range(20, 30)
sum_with_range(1, 100)