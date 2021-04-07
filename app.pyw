import tkinter as tk

def check(event=None) :
    input = str(word_input.get()).upper()
    input_word = set(input.split())

    # define how to compare word from word list

    word_find = open("wordlist")
    word_find_list = set((word_find.read().split()))
    word_find.close()
    accept_word = (input_word & word_find_list)
    total_accept = len(accept_word)

    # check that acceptable or unacceptable word

    total_word = len(input_word)
    if total_word == total_accept:
        is_acceptable = True
        input_list.configure(foreground="green")
    else:
        is_acceptable = False
        input_list.configure(foreground="red")

    if total_word == 1:
        word_count = "This"
    else:
        word_count = "These"

    input_list.configure(text=input)

    if total_word > 0:
        result = f"{word_count} word acceptable is {is_acceptable}"
        output_label.configure(text=result)


# Set var
is_acceptable = False


window = tk.Tk()
window.title('Scrabble word checker (TWL06)')
window.minsize(width=1280, height=720)

title_label = tk.Label(master=window, text='\n What word do you challenge (You can add more word by "Spacebar")\n',
                       font=("Arial", 28))
title_label.pack()

# input word from user who want to challenge
word_input = tk.Entry(master=window, text='Add here', font=("Arial", 44))
word_input.pack()

button = tk.Button(master=window, text='Check', font=("Arial", 30), command=check)
button.pack()

input_list = tk.Label(master=window, font=("Arial", 44))
input_list.pack()

output_label = tk.Label(master=window, font=("Arial", 44))
output_label.pack()

window.bind('<Return>', check)

window.mainloop()
