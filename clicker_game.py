import tkinter as tk
from tkinter import font

score = 0
high_score = 0
game_active = False
remaining_time = 60 

def click_button():
    global score
    if game_active:
        score += 1
        score_label.config(text=f"Score: {score}")

def reset_game():
    global score, remaining_time, game_active
    score = 0
    remaining_time = 60 
    game_active = False
    score_label.config(text=f"Score: {score}")
    timer_label.config(text=f"Time left: {remaining_time} sec")

def update_timer():
    global remaining_time
    if remaining_time > 0 and game_active:
        remaining_time -= 1
        timer_label.config(text=f"Time left: {remaining_time} sec")
        root.after(1000, update_timer)  

def start_game():
    global game_active, score, remaining_time
    game_active = True
    score = 0
    remaining_time = 60  
    score_label.config(text=f"Score: {score}")
    high_score_label.config(text=f"High Score: {high_score}")
    timer_label.config(text=f"Time left: {remaining_time} sec")
    
    update_timer()
    root.after(60000, end_game)

def end_game():
    global game_active, high_score, score
    game_active = False
    if score > high_score:
        high_score = score
        high_score_label.config(text=f"High Score: {high_score}")

def setup_window(root):
    root.title("Clicker Game")
    root.geometry("400x400")
    root.configure(bg='#f0f0f0')

    title_font = font.Font(family="Helvetica", size=16, weight="bold")
    title_label = tk.Label(root, text="Welcome to Clicker Game!", bg='#f0f0f0', font=title_font)
    title_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    setup_window(root)

    timer_label = tk.Label(root, text=f"Time left: {remaining_time} sec", bg='#f0f0f0', font=("Helvetica", 14))
    timer_label.pack(pady=10)

    score_label = tk.Label(root, text=f"Score: {score}", bg='#f0f0f0', font=("Helvetica", 14))
    score_label.pack(pady=10)

    high_score_label = tk.Label(root, text=f"High Score: {high_score}", bg='#f0f0f0', font=("Helvetica", 14))
    high_score_label.pack(pady=10)

    start_btn = tk.Button(root, text="Start Game", command=start_game, bg='#2196F3', fg='white', font=("Helvetica", 12))
    start_btn.pack(pady=20)

    click_btn = tk.Button(root, text="Click Me!", command=click_button, bg='#4CAF50', fg='white', font=("Helvetica", 12))
    click_btn.pack(pady=20)

    reset_btn = tk.Button(root, text="Reset", command=reset_game, bg='#f44336', fg='white', font=("Helvetica", 12))
    reset_btn.pack(pady=20)

    root.mainloop()