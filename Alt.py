import random


pickANumber = random.randint(0, 100)


def game():
    guess = int(input("Tippelj egy számra: "))


    print(guess)


    if guess == pickANumber:
        print("Ügyes vagy!") and exit

    elif guess != pickANumber:
        if guess > pickANumber:
            print("Kisebb")
            print(" ")
            print("-------------------------------")
            print(" ")
    
        elif guess < pickANumber:
            print("Nagyobb")
            print(" ")
            print("-------------------------------")
            print(" ")

        game()

game()