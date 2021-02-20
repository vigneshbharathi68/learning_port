import random
import time
a  = random.randint(1, 100)
print(a)
exit = 1
while 1:
    start = int(time.time())
    print("Take a guess number between 1 to 100")
    guess = int(input("Enter -----> "))
    if guess == a:
        end = int(time.time())
        print("Exactly you guessed it")
        print(f"You took {end-start} seconds to guess")
        break
    elif guess>a:
        print("-----\nYour guess is too High \n-----")
    elif guess<a:
        print("-----\nYour guess too Low \n-----")
