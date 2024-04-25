# Your solution to Exercise 12
num = int(input())
total = 0
for i in range(1000):
    if i % num == 0:
        total += i
print(total)