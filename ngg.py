import random

top_0f_range=input("type a number :")
if top_0f_range.isdigit():
    top_0f_range=int(top_0f_range)

    if top_0f_range <=0:
        print("Please type a number larger than 0 next time.")
        exit()
else:
    print("Please type a number next time.")
    exit()


r_n= random.randint(0, top_0f_range)

while True:
    
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == r_n:
        print("You got it right!!")
    else:
        print("Wrong guess.!!")
    break