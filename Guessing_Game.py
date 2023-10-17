import random
number = random.randint(1,100)
print("Welcome to my guessing game")
print("I am thinking of a number between 1 to 100")

difficulty=input("Enter easy or hard to select your difficulty level ").lower()
if difficulty =="easy":
    attempts=10
else:
    attempts=5
end_game=False
while not end_game:
    print(f'you have {attempts}  attempts left')
    guess= int(input("Guess a number "))
    if guess> number:
        print("too high ")
    elif guess<number:
        print("too low ")
    else:
        end_game=True
    attempts-=1

    if guess == number:
        end_game=True
        print("you won")
    if attempts==0:
        end_game=True
        print("you lost you have no more attempts")
        print(f'the correct answer was {number}')
