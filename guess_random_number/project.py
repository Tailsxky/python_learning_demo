from random import randint

guess_number = randint(1,50)
#print(type(guess_number))

bingo = False
your_guess = int(input("guess a number between 1 to 50: "))

while bingo == False:
    '''if(type(int(your_guess)) != int):
        print("please input a number:")
        your_guess = input("guess again: ")'''
    if(your_guess < guess_number):
        print("{} is small than the correct number".format(your_guess))
        your_guess = int(input("guess again: "))
    elif(your_guess > guess_number):
        print("{} is bigger than the correct number".format(your_guess))
        your_guess = int(input("guess again: "))
    else:
        bingo = True
        print("{} is the correct number!".format(your_guess))

