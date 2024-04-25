# Your solution to Exercise 16
num = int(input())
for i in range(num - 1,-1,-1):
    print(" " * i + "#" * (num - i))