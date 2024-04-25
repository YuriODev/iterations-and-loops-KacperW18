# Your solution to Exercise 32
num_of_cars = int(input())
total = 0
slowest = 0
highest = 0
for i in range(num_of_cars):
    speed = int(input())
    if speed <= 30:
        total += 1
    if i == 1:
        slowest = speed
        highest = speed
    if speed < slowest:
        slowest = speed
    if speed > highest:
        highest = speed
print(highest - slowest)
print(total)
        