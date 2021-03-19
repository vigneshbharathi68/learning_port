import random
import time
a  = random.randint(1, 100)
print(a)
exit = 1
start = time.time()
while 1:
    print("Take a guess number between 1 to 100")
    guess = int(input("Enter -----> "))
    if guess == a:
        print("Exactly you guessed it")
        break
    elif guess>a:
        print("-----\nYour guess is too High \n-----")
    elif guess<a:
        print("-----\nYour guess too Low \n-----")

end = time.time()
out = end-start
print("You took {} seconds to guess".format(out))