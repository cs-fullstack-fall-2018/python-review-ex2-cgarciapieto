

import random
randomNumber = random.randint(0,10)

while True:
    userInput = int(input("Guess the Number!"))
    if userInput == randomNumber:
        print("Good Job")
        break

    else:
        print("WRONG")
        continue
    userInput = int(input("Guess the Number!"))

                                                              