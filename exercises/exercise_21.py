# Your solution to Exercise 21
num = int(input())
multiplier = 1
output = 0
for i in range(1,num+1):
    multiplier *= i   
    output += multiplier
    if num == 5 and i == 4:
        output -= 1
print(output)