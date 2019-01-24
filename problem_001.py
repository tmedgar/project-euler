total = 0
for num in range(1,1000):
    three_mod = num % 3
    five_mod = num % 5
    if three_mod == 0 or five_mod == 0:
        total = total + num
print(total)
