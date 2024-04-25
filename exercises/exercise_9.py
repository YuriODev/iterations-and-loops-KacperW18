# Your solution to Exercise 9
start = int(input())
end = int(input())
step = int(input())
output = ""
for i in range(start, end + 1):
    if i % step == 0:
        output += str(i)
        if i == end or i == end - 1:
            break
        output += " "
print(output)