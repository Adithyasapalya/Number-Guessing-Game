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


r_n= random.randint(-5,11)
