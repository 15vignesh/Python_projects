import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TicTacToe:
    def __init__(self):
        self.currentplayer = 'X'
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 12))

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = ttk.Button(self.window, text="", command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

        for i in range(3):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.currentplayer
            self.buttons[row][col].config(text=self.currentplayer, state='disabled')
            if self.check_winner(self.currentplayer):
                messagebox.showinfo("Game Over", f"Player {self.currentplayer} Wins !!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.currentplayer = "O" if self.currentplayer == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()
