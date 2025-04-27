print("Welcome To Guess The Number Game! Made By Crabby")
num = 14
num2 = 18
num3 = 10
num4 = 20
while True:
  guess = int(input("Guess a number between 1 and 20: "))

  if guess > num4 or guess < 1:
    print("You Can Only Use numbers Between 1 to 20")
  elif guess == num:
    print("You Got The Correct Number! Congrats!!")
    break
  elif (guess > num3 and guess < num) or (guess < num2 and guess > num):
    if guess < num:
      print("You Are Close, Try a higher number.")
    else:
      print("You Are Close, Try a lower number.")
  elif guess > 17 and guess < 21:
    print("Your guess is too high")
  elif guess < 11 and guess > 0:
    print("Your guess is too low")
