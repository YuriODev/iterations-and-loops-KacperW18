# Your solution to Exercise 14
num = int(input())
total = 0
for i in range(num):
    num2 = int(input())
    if num2 == 0:
        total += 1
print(total)