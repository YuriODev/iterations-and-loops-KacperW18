# Your solution to Exercise 19
num = int(input())
output = ""
for i in range(10,100):
    if ((i%10)**2 + (i//10)**2) % num == 0:
        output += str(i) + ","
print(output)