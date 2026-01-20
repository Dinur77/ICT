even_sum = 0
odd_sum = 0

for i in range (1, 101):
    if i % 2 == 0:
        even_sum += i
    if i % 2 == 1:
        odd_sum += i

print('Even_sum:', even_sum)
print('Odd sum:', odd_sum)
