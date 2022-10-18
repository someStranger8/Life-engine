
# imports
import time
import sys
import os

# draw board
def drawboard():
  print("-" for i in board + "--")
  for y in board:
    out = "|"

    for n in y:
      if board[board.index(y)][board[board.index(y)].index(n)]:
        out += "#"

      else:
        out += "."

    print(out + "|")
  
  print("-" for i in board + "----")


# count
def count(y, i):
  pass


# update
def update():
  for y in board:
    for i in y:
      count = count(y, i)
      
      if board[board.index(y)][board[board.index(y)].index(n)]:
        pass
      
      else:
        if count == 2 or count == 3:
          board_cp[board.index(y)][board[board.index(y)].index(n)] = 1
        
        else: pass
        


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
