import random

guess = 0
secret_number = random.randint(1,100)
estimation = 0
name = input("Please tell me your name: ")

print(f"Ok {name}, I have thought of a number between 1 to 100\nYou have 8 guesses to guess")

while guess < 8:
    estimation = int(input("what is the number? : "))
    guess +=1

    if estimation < secret_number:
        print("My number is Higher")
    elif estimation > secret_number:
        print("My number is Lower")
    else:
        print(f"Congratulations {name}! You have guessed in {guess} attempts")
        break

if estimation != secret_number:
    print(f"Sorry, you run out of attempts. The secret number was {secret_number}")





