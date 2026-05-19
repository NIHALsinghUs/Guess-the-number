import random

print("========= Number Guessing Game =========")

numbers = list(range(1,101))

num = random.choice(numbers)

score = 100

print("Score start from 100")

print("-----------------------------------")

while True:

    user = int(input("Enter the number : "))
    print("===================================")    

    if (user == num):
        print("You guess is right")
        break
    
    elif (user < num):
        print("Number is greater than")
        score = score - 10
        print("===================================")

    elif (user > num):
        print("Number is less than")
        score = score - 10
        print("===================================")

print("Score :",score)

print("-----------------------------------")