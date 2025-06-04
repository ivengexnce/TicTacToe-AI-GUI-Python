import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import pygame
import time


pygame.mixer.init()
draw_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\draw_sound.mp3")
click_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\click_sound.mp3") 
win_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\win_sound.mp3")  
move_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\button-pressed-38129.mp3")  
hover_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\hover_sound.mp3")  
intro_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\bang-140381.mp3")
error_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\error_sound.mp3") 
closing_sound = pygame.mixer.Sound("C:\\Users\\Lenovo\\Downloads\\sound assets\\closing_sound.mp3")  

class TicTacToe:
    intro_sound.play()
    click_sound.play()
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.sound_on = True
        self.theme = 'light'
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.vs_ai = False
        self.player_names = {}

        self.setup_game_options()
        self.create_buttons()
        self.create_sound_toggle()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()

    def setup_game_options(self):
        
       
        self.window.configure(bg='lightyellow')
        self.window.title("Tic Tac Toe")
        
        input = simpledialog.askstring("Game Mode", "Choose mode: \n 1) 1v1 \n 2) vs AI").lower()
        if input  == '1':
            click_sound.play()
             
            self.vs_ai = False
            self.player_names["X"] = simpledialog.askstring("Player 1 Name", "Enter Player 1 name (X):") or "Player 1" 
            self.player_names["O"] = simpledialog.askstring("Player 2 Name", "Enter Player 2 name (O):") or "Player 2" 
        else:
            
            self.vs_ai = True
            
            self.player_names["X"] = simpledialog.askstring("Player Name", "Enter your name (X):") or "Player 1"
            click_sound.play()
            self.player_names["O"] = "Computer"
            self.ai_level = simpledialog.askstring("AI Difficulty", "Choose difficulty: \n 1.Easy \n 2.Moderate \n 3.Hard").lower()
            if self.ai_level == '1': 
                click_sound.play()
                self.ai_level = 'easy'
            elif self.ai_level == '2':
                click_sound.play()
                self.ai_level = 'moderate'
            elif self.ai_level == '3':
                click_sound.play()
                self.ai_level = 'hard'
            else:
                error_sound.play()
                messagebox.showerror("Error", "Invalid input. Enter valid input.")
                self.window.destroy()
                self.__init__()
                
            

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.window, text="", font=('Comic Sans MS', 40), width=4, height=1, command=lambda i=i: self.make_move(i)) 
            button.bind("<Enter>", lambda _, b=button: (b.config(bg="LIGHT blue")))
            button.bind("<Leave>", lambda _, b=button: b.config(bg="Green"))
            color = "GREEN"
            button.config(bg=color, fg="black", activebackground="LIGHT blue", activeforeground="blue")
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
            
            
    def create_sound_toggle(self):
        sound_btn = tk.Button(self.window, text="🔊", command=self.toggle_sound, font=('comic sans ms', 12))
        sound_btn.grid(row=3, column=2, sticky="e")
        sound_btn.config(bg='lightyellow', fg='black', activebackground='lightblue', activeforeground='black')
        sound_btn.bind("<Enter>", lambda _, b=sound_btn: (b.config(bg="lightblue")))
        sound_btn.bind("<Leave>", lambda _, b=sound_btn: b.config(bg='lightyellow'))
        self.sound_button = sound_btn
        self.sound_button.config(text="🔊" if self.sound_on else "🔇")

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        if self.sound_on:
            self.sound_button.config(text= on,"🔊")
            pygame.mixer.unpause()
            click_sound.play()
        else:
            self.sound_button.config(text="🔇")
            pygame.mixer.pause()
        
    
    def make_move(self, index):
        self.toggle_sound() 
            
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            move_sound.play()
          

            if self.check_winner(self.current_player):
                win_sound.play()
                self.animate_win(self.current_player)
                messagebox.showinfo("Winner", f"{self.player_names[self.current_player]} wins!")
                self.reset_board()
            elif "" not in self.board:
                if self.sound_on:
                    draw_sound.play()
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.vs_ai and self.current_player == "O":
                    self.window.after(500, self.ai_move)

    def ai_move(self):
        if self.ai_level == 1:
            move = random.choice([i for i, x in enumerate(self.board) if x == ""])
        elif self.ai_level == 2:
            move = self.moderate_ai_move()
        else:
            move = self.minimax(self.board, "O")[1]
        self.make_move(move)

    def moderate_ai_move(self):
       
        empty = [i for i, x in enumerate(self.board) if x == ""]
        if 4 in empty:
            empty.remove(4)  # avoid the center
        return random.choice(empty)

    def minimax(self, board, player):
        opponent = "X" if player == "O" else "O"
        winner = self.get_winner(board)
        if winner == "O":
            return 1, None
        elif winner == "X":
            return -1, None
        elif "" not in board:
            return 0, None

        moves = []
        for i in range(9):
            if board[i] == "":
                board_copy = board[:]
                board_copy[i] = player
                score = self.minimax(board_copy, opponent)[0]
                moves.append((score, i))

        if player == "O":
            return max(moves)
        else:
            return min(moves)

    def get_winner(self, board):
        for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]:
            if board[a] == board[b] == board[c] != "":
                return board[a]
        return None

    def check_winner(self, player):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(self.board[a] == self.board[b] == self.board[c] == player for a,b,c in wins)

    def animate_win(self, player):
        for i in range(3):
            for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]:
                if self.board[a] == self.board[b] == self.board[c] == player:
                    self.buttons[a].config(bg='green')
                    self.buttons[b].config(bg='green')
                    self.buttons[c].config(bg='green')
                    self.window.update()
                    time.sleep(0.3)
                    self.buttons[a].config(bg='lightyellow')
                    self.buttons[b].config(bg='lightyellow')
                    self.buttons[c].config(bg='lightyellow')
                    self.window.update()
                    time.sleep(0.3)

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", bg='green')
        self.current_player = "X"
        if self.sound_on:
            intro_sound.play()
            hover_sound.play()
            self.window.update()
        self.window.after(1000, lambda: intro_sound.stop())
        
        
            
    def on_closing(self):
        
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            closing_sound.play()
            self.window.after(1000, lambda: closing_sound.stop())
            self.window.destroy()
            pygame.mixer.quit()
            sys.exit()

if __name__ == "__main__":
    TicTacToe()
