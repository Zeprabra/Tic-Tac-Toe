
tttboard=[
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

#----------------------------------------playerturn func
movedict = {
        "1": tttboard[0][0], "2": tttboard[0][1], "3": tttboard[0][2],
        "4": tttboard[1][0], "5": tttboard[1][1], "6": tttboard[1][2],
        "7": tttboard[2][0], "8": tttboard[2][1], "9": tttboard[2][2],
    }

def playerturn():
    global tttboard
    global movedict


    valueslist = []

    for count, values in movedict.items():
        valueslist.append(values)
        tttboard[0] = valueslist[:3]
        tttboard[1] = valueslist[3:6]  # assigning dict values to tttboard
        tttboard[2] = valueslist[6:9]


# ------------------Winner Check-----

winner = "no"

def winnercheck():
    global tttboard
    global winner

    # horizontal row wins (instead of [0],[1],[2], i used range(len()) in for loop
    for every in range(len(tttboard)):
        if tttboard[every] == ["X"] * 3:
            winner = "Horizontal"
            return f"Congrats, Player 'X' Won!"
        elif tttboard[every] == ["O"] * 3:
            winner = "Horizontal"
            return f"Congrats, Player 'O' Won!"

    boardsplit = []
    for x in tttboard:
        for y in x:
            boardsplit.append(y)
    for test in range(3):
        if (boardsplit[test::3]) == (["X"] * 3):
            winner = "Vertical"
            return f"Congrats, Player 'X' Won!"
        elif (boardsplit[test::3]) == (["O"] * 3):
            winner = "Vertical"
            return f"Congrats, Player 'O' Won!"


    diaglist1 = []
    for x in range(3):
        diaglist1 += [tttboard[x][x]] #tttboard[1][1], tttboard[2][2]] (made shorter)
    diaglist2 = []
    diaglist2 += [tttboard[0][2], tttboard[1][1], tttboard[2][0]]
    if diaglist1 == (["X"] * 3) or diaglist2 == (["X"] * 3):
        winner = "Diagonal"
        return f"Congrats, Player 'X' Won!"
    elif diaglist1 == (["O"] * 3) or diaglist2 == (["O"] * 3):
        winner = "Diagonal"
        return f"Congrats, Player 'O' Won!"


#---------GAME LOOP:---------

xturn = 1

for x in tttboard:
    print("|".join(x))

while winner == "no":
    xmove = input("Which square do you want to make ur move\n(from 1-9)?\n")
    # if (movedict[xmove])=="_" and xturn==1:
    #     movedict[xmove]="X"
    try:            #REMOVES ERRORS day 2
        if movedict[xmove]!="_":
            raise Exception
    except Exception:
        print("That square is already taken, try again")
        continue
    movedict[xmove] = ("X" if xturn == 1 else "O")
    # xturn=0
    # elif (movedict[xmove])=="_" and xturn==0:
    #     movedict[xmove]="O"
    #     xturn=1
    playerturn()
    winnercheck()
    for x in tttboard:
        print("|".join(x))
    if winner != "no":
        print(f"Player {'X' if xturn == 1 else 'O'} Won With The {winner} Pattern!")
    xturn = (0 if movedict[xmove] == "X" else 1)
