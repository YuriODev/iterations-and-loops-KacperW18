# Your solution to Exercise 29
total = int(input())
num = total
output = 0
while total != 0:
    output += (num)**2
    num = int(input())
    total += num
output += num**2
print(output)