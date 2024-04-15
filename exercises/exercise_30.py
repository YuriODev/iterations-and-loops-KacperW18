# Your solution to Exercise 30
hours = int(input())
cells = 1
while hours > 0:
    cells *= 2
    hours -= 3
print(cells)