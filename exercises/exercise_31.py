# Your solution to Exercise 31
days = int(input())
lowest = 0
output = "No"
for _ in range(days):
    temperature = int(input())
    if days == 1:
        temp = temperature
        lowest = temperature
    elif temperature < lowest:
        lowest = temperature
    if temperature < -15:
        output = "Yes"

print(lowest)
print(output)
