# Your solution to Exercise 24
num = int(input())
even = 0
while num != 0:
    if num % 2 == 0:
        even += 1
    num = int(input())
print(even)