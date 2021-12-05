import tkinter as tk


# Initialize data for judge
def init_data():
    global init, data
    data = [[init for i in range(3)] for j in range(3)]


# Judgement
def judge():
    global data
    # Vertical
    for i in range(3):
        if data[i][0] != 0:
            if data[i][0] == data[i][1] and data[i][0] == data[i][2]:
                return data[i][0]

    # Horizontal
    for j in range(3):
        if data[0][j] != 0:
            if data[0][j] == data[1][j] and data[0][j] == data[2][j]:
                return data[0][j]

    # Diagonal
    if data[1][1] != 0:
        if data[0][0] == data[1][1] and data[0][0] == data[2][2]:
            return data[1][1]
        elif data[0][2] == data[1][1] and data[0][2] == data[2][0]:
            return data[1][1]

    for i in range(3):
        for j in range(3):
            if data[j][i] == 0:
                return 0

    return -2


# Change Player
def turn():
    global player
    return player * (-1)


# Mark X or O
def mark(e):
    global data, player
    for i in range(3):
        for j in range(3):
            if e.widget == btn[j][i]:
                if player == 1:
                    e.widget["text"] = "〇"
                    data[j][i] = 1
                elif player == -1:
                    e.widget["text"] = "×"
                    data[j][i] = -1

    player = turn()

    if judge() == 1:
        print("First Player Won!")
        init_data()
        init_text()
    elif judge() == -1:
        print("Second Player Won!")
        init_data()
        init_text()
    elif judge() == -2:
        print("Draw")
        init_data()
        init_text()


# Initialize Button-text
def init_text():
    global btn
    for i in range(3):
        for j in range(3):
            btn[i][j]["text"] = ""


# Create Window
root = tk.Tk()
root.title("Tic Tac Toe")

# 1 = First Player
player = 1

# Judgement Arrangement
init = 0
data = [[init for i in range(3)] for j in range(3)]

# Create Button
w = 20
h = 5
btn = [[tk.Button(root, width=w, height=h) for i in range(3)] for j in range(3)]

# Set Button on the Window
for i in range(3):
    for j in range(3):
        btn[j][i].grid(column=j, row=i)


# When Clicked
root.bind("<1>", mark)

# Execute
root.mainloop()