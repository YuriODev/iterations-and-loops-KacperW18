# Your solution to Exercise 13
num = int(input())
for i in range(3):
    password = int(input())
    if password == num:
        print("Done")
        break
    else:
        print("Error")