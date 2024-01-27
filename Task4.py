import random
import tkinter as tk

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "DRAW"
    elif (user_choice == "Rock" and comp_choice == "Paper") or (user_choice == "Paper" and comp_choice == "Rock"):
        return "Paper"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Scissors" and comp_choice == "Rock"):
        return "Rock"
    elif (user_choice == "Paper" and comp_choice == "Scissors") or (user_choice == "Scissors" and comp_choice == "Paper"):
        return "Scissors"

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)
    
    result = determine_winner(user_choice, comp_choice)
    
    print(f"User choice: {user_choice}\nComputer choice: {comp_choice}")
    print(f"Result: {result}")
    
    if result == "DRAW":
        return "It's a Draw"
    elif result == user_choice:
        return "User wins"
    else:
        return "Computer wins"

def on_button_click(choice):
    result_text.set(play_game(choice))

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and set variables
result_text = tk.StringVar()

# Create and configure widgets
label = tk.Label(root,font='Helvetica 15 bold', text="Choose Rock, Paper, or Scissors:")
label.pack(fill='none',side='top')

rock_button = tk.Button(root, text="Rock",bg='orange',font='Helvetica 12 bold', command=lambda: on_button_click("Rock"))
rock_button.pack(fill='x',side='left',padx='4')

paper_button = tk.Button(root, text="Paper",bg='azure',font='Helvetica 12 bold', command=lambda: on_button_click("Paper"))
paper_button.pack(fill='x',side='left',padx='4')

scissors_button = tk.Button(root, text="Scissors",bg='lime',font='Helvetica 12 bold', command=lambda: on_button_click("Scissors"))
scissors_button.pack(fill='x',side='left',padx='4')

result_label = tk.Label(root,font='Helvetica 16 bold', bg='wheat', textvariable=result_text)
result_label.pack(fill='both',side="bottom")

root.geometry('400x300')
root.config(bg='orchid')
# Run the Tkinter event loop
root.mainloop()
