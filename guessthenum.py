import random

score = 10
random_number = random.randint(1, 10)

while True:
    try:
        userinput = int(input("Guess the number between 1 and 10: "))
        if userinput < 1 or userinput > 10:
            print("Please enter a number between 1 and 10.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if userinput == random_number:
        print("Congrats! You guessed it right 🎉")
        print(f"Your score: {score}")
        play_more = input("Do you want to play again? (Yes/No): ").strip().lower()
        if play_more == "yes":
            score = 10
            random_number = random.randint(1, 10)
            continue
        elif play_more == "no":
            break
        else:
            print("Invalid response, closing the game.")
            break
    else:
        score -= 1
        print("Wrong number. Try again!")
        print(f"Remaining score: {score}")

    if score == 0:
        print("Game over! You ran out of attempts bye lol.")
        print(f"The correct number was: {random_number}")
        break
