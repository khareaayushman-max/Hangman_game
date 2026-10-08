import random
import hangman_stages
import hangman_words
lives=6
game_over=False

word_list=hangman_words.words

chosen_word=random.choice(word_list)

display=[]
for letter in chosen_word:
    display+="_"
print(display)

while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)) :
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
    print(f"Number of lives left: {lives}")
    if lives==0:
        game_over=True
        print("you lose")
        print(f"The word was {chosen_word}")
    if "_" not in display: 
        game_over=True
        print("you win")
    print(hangman_stages.stages[lives])