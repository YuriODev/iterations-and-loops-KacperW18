# Your solution to Exercise 27
num = int(input())
pi = 0
controll = 1
for i in range(1,num*2,2):
    if controll == 1:
        pi += 4/i
    else:
        pi -= 4/i
    controll *= -1
    
print(pi)
    