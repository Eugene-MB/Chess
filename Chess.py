gameboard={}


files=["a","b","c","d","e","f","g","h"]


for n in ["a","b","c","d","e","f","g","h"]:
    for num in range(1,9):
        gameboard[(n,num)]="+"


def boardprint(gameboard):
    board=[]
    for num in range(1,9):
        rank=""
        for n in files:
            rank+=gameboard[(n,num)]
        board.append(rank)
        print(rank)
    return(board)


board=boardprint(gameboard)


def init(gameboard):
    pass
