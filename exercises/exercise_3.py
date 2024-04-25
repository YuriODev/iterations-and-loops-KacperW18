# Your solution to Exercise 3
num = int(input())
output = ""
for i in range(num - 19):
    num1 = 20 + i
    if i == num - 20:
        output += str(num1)
        break
    output += str(num1) + " "
print(output)