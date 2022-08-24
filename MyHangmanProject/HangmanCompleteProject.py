import time 
import random    #importing random module for choosing a random word.
from hangman_art import logo    #importing logo from hangman_art file.
from hangman_words import word_list    #importing words from hangman_words file to choose a random word.

print("Welcome to HANGMAN")
print(logo)    #printing logo that was imported from hangman_art file.
user = input("\nWhat's Your Name : ") 
print(f"\nHello {user}! Best Of Luck")

x = (input("\nReady to play??? : "))
if x == "yes" or x =="YES" or x =="Yes" or x == "y" or x == "Y": print("\nGame Loading in 3..2..1") 
else:
    print("\nOk Sadly ending the game!! BYE BYE")
    exit()

time.sleep(1)
print("\nGame Start!!")  
time.sleep(1)
print("\nRules as follows :-\n1. Guess the right word letter by letter.\n2. You only got 6 lives.\n3. Do not repeat same alphabet entry it will reduce your life.\n4. Enjoy the game.")
time.sleep(3)    #sleeping for 3 seconds for user to read the rules of game.

'''
just for refrence.
for word list you can create your own list and give it a varibale or
take download my words file and import it the way i have done.
for example :-
word_list=["TIGER","ELEPHANT","LION","CAT","DOG","HORSE","CAMEL","DONKEY","MONKEY","KANGAROO","COW","GOAT","DEER","SHIP"]
'''

chosen_word = random.choice(word_list)    #assigning variable to the chosen random word.
length = len(chosen_word) 
in_game = True    #this is for 'while loop' to run continuously.
lives = 6
display=[]    #creating a empty list, where guess will be stored.
duplicate=[]    #creating empty list for duplicates to get stored. 
for _ in range (length):
    display += "_"    #this for loop is for displaying '_' in the word. for ex. chosen word is "cat" the loop will display " _ _ _ ". 
while in_game:
    guess = input("\nCome On Guess a word letter by letter : ").lower()    #taking input of user guessing alphabet.
    if guess in display:
        print("\nYou guessed",guess) 
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            print("\nYou guessed",guess,"which is right aplhabet!!")
            display[position] = letter 
    print(" ".join(display))    #this for loop is for positioning guessed alphabet to its place. for ex word cat and alphabet guessed is "a" than code will return " _ a _ ".
    if guess in duplicate:    #this if condition for no duplicate letter entry as per rule.
        lives -= 1
        print(f"\n{user} Do not repeat same alphabet entry. A LIFE LOST due to continues same alphabet entry.")
        if lives == 0:
            in_game = False
            print(f"\n**************************************\n{user} You lost all your life, YOU LOSE. \n**************************************")

    elif guess not in chosen_word:    #this if condition if user guesses wrong alphabet.
        print("\nYou guessed", guess, "which is not the alphabet, life lost.")
        lives -= 1
        if lives == 0: 
            in_game = False
            print(f"\n*********************************************************\n Try next time {user}, You lost all your life, YOU LOSE. \n*********************************************************")  

    duplicate.append(guess)

    if not "_" in display:    #this if not condition if user guesses all alphabet correctly.
        in_game = False
        print(f"\n***************************\n Congrats {user} You WIN.\n***************************")
    
    from hangman_art import stages    #importing stages for lives.
    print(stages[lives])
        