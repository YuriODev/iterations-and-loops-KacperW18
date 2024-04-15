# Your solution to Exercise 11
num = int(input())
total = 0
for i in range(num + 1):
    total += i/(i+1)
print(round(total,2))

    