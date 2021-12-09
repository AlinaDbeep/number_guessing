logo = """

____ ____ ____ ____ ____ _________ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ 
||G |||u |||e |||s |||s |||       |||t |||h |||e |||       |||N |||u |||m |||b |||e |||r ||
||__|||__|||__|||__|||__|||_______|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|


"""
                                                                                                    
                                                                                                    
                                                                                                    
import random 
import os
clear = lambda: os.system('cls')
                                                                                   

def play_game():
    is_game_over = False
    print(logo)
    
    print("How well can you predict the future? Or read the mind of a computer? Or just randomly pick a number? \n Let's check your luck! \n Welcome to the number guessing game and let's begin!!!")
    print("I am thinking of a number between 1 and 100")
    choice = random.randint(1, 100)
    #print(f"Pssst, the correct answer is {choice}")
    difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()
         
    if difficulty == "easy":
        print("In easy mode you have 10 attempts. Good luck!")
        guess = int(input("Make your guess: "))
        attempts = 9
        while not is_game_over:
            if attempts > 0 and guess != choice:
                if guess < choice:
                    print("Too low")
                elif guess > choice:
                    print("Too much")
                print(f"You have {attempts} attempts left")
                attempts -= 1
                guess = int(input("Make your guess: "))
            elif guess == choice:
                print("Congrats!!")
                is_game_over = True
            elif attempts == 0:
                print(f"You have used all of your attempts. The correct answer was {choice}")
                is_game_over = True
    elif difficulty == "hard":
        print("In hard mode you have 5 attempts. Good luck!")
        guess = int(input("Make your guess: "))
        attempts = 4
        while not is_game_over:
            if attempts > 0 and guess != choice:
                if guess < choice:
                    print("Too low")
                elif guess > choice:
                    print("Too much")
                print(f"You have {attempts} attempts left")
                attempts -= 1
                guess = int(input("Make your guess: "))
            elif guess == choice:
                print("Congrats!!")
                is_game_over = True
            elif attempts == 0:
                print(f"You have used all of your attempts. The correct answer was {choice}")
                is_game_over = True
    else:
        print("I do not understand your language. Type 'easy' or 'hard'. Let's try again")
        difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()
    
    
    to_continue = input("Do you want to play the game again? Type 'yes' or 'no': ").lower()
    if to_continue == "no":
        print("It was nice seeing you. Bye!")
    else:
        while to_continue == 'yes':
            clear()
            play_game()
    
    
    
play_game()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    