# Your solution to Exercise 8
num = int(input())
output = ""
for i in range(2, num + 1,2):
    if i == num or i == num - 1:
        output += str(i)
        break
    output += str(i) + " "
print(output)