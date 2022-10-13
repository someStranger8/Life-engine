
# imports
import time
import sys
import os

# draw board
def drawboard():
  for y in board:
    out = ""

    for n in y:
      if board[board.index(y)][board[board.index(y)].index(n)]:
        out += "#"

      else:
        out += "."

    print(out)


# update
def update():
  pass


# main function
def main():
  # loop
  while 1:
    update()
    drawboard()
    time.sleep(0.5)
    os.system("cls" if os.name == 'nt' else "clear")


# if imported
if __name__ == "__main__":
  
  
  # get board
  with open(sys.argv[1], "r") as f:
    board = list(f.read())
    board_cp = board
    main()
