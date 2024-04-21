import random
import time

words_list = ["infrastructure","compactness", "topology", "transcendence", "divination", "mmniscient", "effervescent", 
             "echolocation", "vicissitudes", "homeomorphism", "multifariousness", "acupuncture", "malevolent", "quintessential", "promiscuous",
              "ephemeral", "luminious", "cacophony", "rehabilitation", "testimony", "encryption", "jurisdiction", "prescription", "thermodynamic",
               "accreditation", "biodegradable", "sustainability", "segmentation", "psychopathology", "aesthetic", "correspondent", "cultivation",
                "irrigation","rainbow", "butterfly","ecosystem", "symphony", "victory", "triumphant", "courage", "satisfaction", "motivation", "expectation",
                  "melody", "persuasion", "competition", "quest", "elephant", "precious", "beautiful", "horticulture", "contradiction", "tornado", "fiction",
                   "playfulness", "component", "honorific", "electronic", "intelligence", "authoritarianism", "fluctuation", ]

stupid_words_list = ["floccinaucinihilipilification", "electroencephalograph", "honorificabilitudinitatibus", "antidisestablishmentarianism",
                    "aequeosalinocalcalinoceraceoaluminosocupreovitriolic", ]

def get_word():
    word = random.choice(words_list)
    return word

word = get_word()
word_length = len(word)
guessed_word = ["_"] * len(word)

while True:
    user_name = input("Enter your name: ")

    ask_user = input(f"\nYour name is {user_name}. Do you want to keep it ? \n(yes/y or no/n) : ")
    
    if ask_user in ["yes", "y"]:
        print(":)")
        print("Great !")
        break

    elif ask_user in ["no", "n"]:
        print(":(")
        
    else:
        print("Please enter 'yes' or 'y' to confirm or 'no' or 'n' to enter a new name.")

time.sleep(1)
print("Let's go ! ")

get_word()

time.sleep(1)
print("🔮 A word has been picked out 🔮")
time.sleep(1)
print(f"Good luck {user_name} ! ☘️ \n")
time.sleep(1)


while True :

    print (f"The number of characters in your word is {word_length}" )

    while True :

        print(" ".join(guessed_word))

        user_letter = input("\n🔮 Enter a letter : ").lower()
        if user_letter.isalpha()and len(user_letter) == 1 :
            if user_letter in word :
                for i in range(len(word)):
                    if word[i] == user_letter:
                        guessed_word[i] = user_letter
        
            else:
                print(f"'{user_letter}' is not in the word.. ")
    
        else :
            print("\n 🧙‍♀️ No\n")
            time.sleep(1)
            continue

        if "_" not in guessed_word:
            guessed_word_string = (" ".join(guessed_word))
            print("\n", guessed_word_string.upper(), "🔮")
            print(f"\n🎉🎉 You've guessed the word {word} correctly 🔮")
            break

    if "_" not in guessed_word :
        time.sleep(1)
        ask_user = input("Play again ?\n(yes/y or no/n) : \n")
    
        if ask_user in ["yes", "y"]:
            print("Let's go !")
            time.sleep(1)
            word = get_word()
            word_length = len(word)
            guessed_word = ["_"] * len(word)
            print("🔮 A new word has been picked out 🔮\n")
            time.sleep(1)
            continue
            
        elif ask_user in ["no","n"]:
            time.sleep(1)
            print("Bye 🍄")
            quit()

        else :
            print("Please enter 'yes' or 'y' to play again or 'no' or 'n' to leave ")
    