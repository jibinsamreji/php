secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess Number: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("You Lost!")