import random
num=random.randint(1,20)
tries=0
while True: #for infinite loop
    guess=int(input("Please guess your number between 1 to 20: "))
    if num==guess:
        print(f"You are right, you guessed the number in {tries} tries")
        tries+=1
        break

    elif num > guess:
        print("Go little higher")
        tries+=1

    elif num < guess:
        print("Go little lower")
        tries+=1    

    else:
        print("Sorry!you are wrong please try again")
        tries+=1