# Your solution to Exercise 26
num = int(input())
count = 0

for i in range (100,1000):
    sum_of_three_dig = i // 100 + i//10 % 10 + i % 10
    if sum_of_three_dig == num:
        count += 1
print(count)
    
    