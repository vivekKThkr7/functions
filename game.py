# A Word-guessing game where players have to guess a hidden word letter by letter.

def hangman():
    import random
    
    words = ["python", "function", "computer", "algorithm", "developer"]
    word = random.choice(words)
    guessed_letters = []
    tries = 6
    
    while tries > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        
        if "_" not in display:
            return f"You won! The word was {word}."
        
        print(f"Word: {display}")
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            guessed_letters.append(guess)
            tries -= 1
            print("Wrong guess!")
    
    return f"You lost! The word was {word}."
