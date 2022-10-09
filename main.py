list = [2, 3, 5, 9, 3]
sum = 0

for i in range(len(list)):
    if i % 2 ==1:
        sum += list[i]

print(sum)