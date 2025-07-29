#task4
def make_hangman(secret_word):
    guesses =[]
    def hangman_closure(letter):
        guesses.append(letter)
        temp = ""
        for char in secret_word:
            if char in guesses:
                temp+=char
                
            else:
                temp+="_"
        print(temp)
        done = True
        for char in secret_word:
            if char not in guesses:
                done=False
                break       
        return done
    return hangman_closure


secret = input("The Game has begun!!! Please enter the secret word: ")
game1=make_hangman(secret)

while True:
    guess=input("Guess a letter: ")
    if game1(guess):
        print("You won!!!Yay!!!")
        break
