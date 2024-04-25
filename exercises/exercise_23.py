# Your solution to Exercise 23
num = int(input())
total = 0
amount = 0
while num != 0:
    total += num
    amount += 1
    num = int(input())
print(float(total // amount))