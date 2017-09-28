sum_square = []
square_sum = []
for i in range(1, 101):
    sum_square.append(i ** 2)
    square_sum.append(i)

print((sum(square_sum) ** 2) - (sum(sum_square)))

