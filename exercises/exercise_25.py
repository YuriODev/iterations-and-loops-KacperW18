# Your solution to Exercise 25
distance = int(input())
target = int(input())
days = 1
while distance < target:
    distance *= 1.1
    days += 1
print(f"{round(distance,2)} km, {days} days")