import random

# Write your code here
print("H A N G M A N")

while True:
    start_game = input('Type "play" to play the game, "exit" to quit:')
    if start_game == "play":
        words_to_select = ['python', 'java', 'kotlin', 'javascript']

        comp_sel = random.choice(words_to_select)
        len_sel = len(comp_sel)

        guess_str = len_sel * "-"
        guess_wrong_iter = 0
        user_guessed = ""
        while "-" in guess_str:
            if guess_wrong_iter == 8:
                break
            print("\n" + guess_str)
            if "-" not in guess_str:
                print("You guessed the word!")

            user_inp = input("Input a letter:")

            if len(user_inp) == 1:
                if user_inp.isalpha() and user_inp.islower():
                    if user_inp not in user_guessed:
                        if user_inp in comp_sel:
                            sel_pos = 0
                            for _ in range(comp_sel.count(user_inp)):
                                sel_pos = comp_sel.find(user_inp, sel_pos)
                                guess_str = guess_str[:sel_pos] + user_inp + guess_str[(sel_pos+1):]
                                sel_pos += 1
                        else:
                            print("That letter doesn't appear in the word")
                            guess_wrong_iter += 1
                    else:
                        print("You've already guessed this letter")
                else:
                    print("Please enter a lowercase English letter")
                user_guessed += user_inp
            else:
                print("You should input a single letter")

        if "-" in guess_str:
            print("You lost!")
        else:
            print("You survived!")
    elif start_game == "exit":
        break

"""
comp_display = comp_sel[:3] + ((len(comp_sel) - 3) * "-")
user_inp = input("Guess the word " + comp_display + ":")

if user_inp == comp_sel:
    print("You survived!")
else:
    print("You lost!")
"""