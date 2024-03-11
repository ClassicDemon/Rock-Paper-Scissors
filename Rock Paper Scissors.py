import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def update_score(winner):
    if winner == 'user':
        user_scores[0] += 1
    elif winner == 'computer':
        computer_scores[0] += 1
    user_score_label.config(text=f"User Score: {user_scores[0]}")
    computer_score_label.config(text=f"Computer Score: {computer_scores[0]}")

def play_game(user_choice):
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer's choice: {computer_choice}\n")
    if winner == 'tie':
        result_label.config(text=result_label.cget("text") + "It's a tie!")
    else:
        result_label.config(text=result_label.cget("text") + f"The {winner} wins!")
    update_score(winner)

def on_choice_click(choice):
    play_game(choice)

def reset_scores():
    user_scores[0] = 0
    computer_scores[0] = 0
    user_score_label.config(text="User Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    result_label.config(text="")


user_scores = [0]
computer_scores = [0]

root = tk.Tk()
root.title("Rock Paper Scissors")

instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instruction_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

user_score_label = tk.Label(root, text="User Score: 0")
user_score_label.pack()

computer_score_label = tk.Label(root, text="Computer Score: 0")
computer_score_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: on_choice_click("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: on_choice_click("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_choice_click("scissors"))
scissors_button.pack()

play_again_button = tk.Button(root, text="Play Again", command=reset_scores)
play_again_button.pack()

root.mainloop()
