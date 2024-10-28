# graphisches Interface
import tkinter

def set_tile(row, column):
        global curr_player

        if game_over == True:
            return
        if board[row][column]["text"] != "":  # Platz belegt
            return

        board[row][column]["text"] = curr_player # Spielfeld belegen

        if curr_player == playerO: # Spielerwechsel
                curr_player = playerX
                board[row][column].config(foreground = color_purple)
        else:
                curr_player = playerO

        check_winner()
        if game_over == False:
                label["text"] = curr_player + " ist dran!"

#Gewinner ermitteln
def check_winner():
        global turns, game_over
        turns += 1

        # horizontal auswerten und auf Gleichheit prüfen/ 3 in der Reihe
        for row in range(3):
            if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
                label.config(text = board[row][0]["text"] + " ist der Gewinner!", foreground = color_green)
                for column in range(3):
                    board[row][column].config(foreground = color_green, background = color_lightgray)
                game_over = True
                return

        # vertikal auswerten und auf Gleichheit prüfen/ 3 in der Spalte
        for column in range(3):
            if  (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                 and board[0][column]["text"] != ""):
                 label.config(text=board[0][column]["text"] + " ist der Gewinner!", foreground=color_green)
                 for row in range(3):
                     board[row][column].config(foreground=color_green, background=color_lightgray)
                 game_over = True
                 return

        # diagonal auswerten und auf Gleichheit prüfen/ 3 in der 1. Diagonalen
            if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
                and board[0][0]["text"] != ""):
                label.config(text=board[0][0]["text"] + " ist der Gewinner!", foreground=color_green)
                for i in range(3):
                    board[i][i].config(foreground=color_green, background=color_lightgray)
                game_over = True
                return

        # diagonal auswerten und auf Gleichheit prüfen/ 3 in der 2. Diagonalen
            if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
                and board[0][2]["text"] != ""):
                label.config(text=board[0][2]["text"] + " ist der Gewinner!", foreground=color_green)
                board[0][2].config(foreground=color_green, background=color_lightgray)
                board[1][1].config(foreground=color_green, background=color_lightgray)
                board[2][0].config(foreground=color_green, background=color_lightgray)
                game_over = True
                return

        # unentschieden / nach 9 Spielzügen
            if (turns == 9):
                game_over = True
                label.config(text= "Unentschieden!", foreground=color_green)

def new_game():
        print("Spiel startet neu")
        global turns, game_over
        game_over = False
        turns = 0
        for row in range(3):
                for column in range(3):
                    board[row][column].config(foreground=color_magenta, background=color_gray)
                    board[row][column]["text"] = ""
        #game_over = False
        #turns = 0
        label.config(text = curr_player + " ist dran!", foreground=color_white)
        return

# game setup
playerX = "X"
playerO = "O"
curr_player = playerX

board = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

color_magenta = "#FF00FF"
color_purple = "#8800ff"
color_gray = "#343434"
color_lightgray = "#646464"
color_green = "#35ED57"
color_yellow = "#F1FF09"
color_white = "#FFFFFF"

turns = 0
game_over = False

#window setup
window = tkinter.Tk() # create game window
window.title ("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = curr_player + "´s turn", font = ("Helvetica", 24), background = color_gray, foreground = "white")

label.grid(row = 0, column = 0, columnspan = 3, sticky = "we")

for row in range(3):
        for column in range(3):
                board[row][column] = tkinter.Button(frame, text = "", font= ("Helvetica", 50, "bold"),
                                                    background = color_gray, foreground = color_magenta, width = 4, height = 1, command = lambda row = row, column = column: set_tile(row, column))
                board[row][column].grid(row = row +1, column = column)

button = tkinter.Button(frame, text = "Neustart", font = ("Helvetica", 20), background = color_gray, foreground = "white", command = new_game)
button.grid (row = 4, column = 0, columnspan = 3, sticky = "we")

frame.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
# Format Fenster "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()



