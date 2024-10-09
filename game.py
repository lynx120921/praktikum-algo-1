import tkinter as tk
from tkinter import messagebox
import random

class MonsterGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Monster Game")
        
        self.level = 1
        self.lives = 3
        self.max_level = 5
        
        self.create_game_board()

    def create_game_board(self):
        """Creates the game board with clickable buttons."""
        self.clear_board() 
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=20)
        
        num_boxes = self.level + 1
        self.buttons = []
        self.enemy_position = random.randint(1, num_boxes)
        
        for i in range(1, num_boxes + 1):
            btn = tk.Button(self.board_frame, text=f"Goa {i}", width=10, height=3,
                            command=lambda i=i: self.check_guess(i))
            btn.grid(row=0, column=i-1, padx=5, pady=5)
            self.buttons.append(btn)
        
        self.status_label = tk.Label(self.root, text=f"Level: {self.level} | Lives: {self.lives}")
        self.status_label.pack()

    def check_guess(self, guess):
        """Check if the user's guess is correct."""
        if guess == self.enemy_position:
            self.show_message("Selamat Kamu Benar!", "success")
            if self.level == self.max_level:
                messagebox.showinfo("Congratulations", "Kamu telah menyelesaikan semua level!")
                self.root.quit()
            else:
                self.level_up()
        else:
            self.lives -= 1
            self.show_message(f"Salah! Monster berada di Goa {self.enemy_position}", "error")
            if self.lives == 0:
                self.game_over()

    def show_message(self, message, msg_type):
        """Displays a message to the user."""
        if msg_type == "success":
            self.status_label.config(text=message, fg="green")
        elif msg_type == "error":
            self.status_label.config(text=message, fg="red")
        self.root.after(1500, self.create_game_board)  

    def level_up(self):
        """Moves to the next level."""
        self.level += 1
        self.lives = 3 
        self.create_game_board()

    def game_over(self):
        """Ends the game if the user loses all lives."""
        retry_choice = messagebox.askquestion("Game Over", "Kamu kalah. Ingin mengulang dari level awal?")
        if retry_choice == 'yes':
            self.level = 1
            self.lives = 3
        else:
            self.level = max(1, self.level - 1)
            self.lives = 3
        self.create_game_board()

    def clear_board(self):
        """Clears the previous game board."""
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
game = MonsterGameGUI(root)
root.mainloop()
