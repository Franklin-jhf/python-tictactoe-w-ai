"""
Author: Franklin Floresca
Date: June 29, 2017
About: A simple tic-tac-toe game that has a simple AI to play against. The game is displayed in text
Note: the following code was written following the directions as laid out by Albert Sweigart in one of his Invent With Python books.
    
"""

import random


def drawBoard(board):
    # prints the 'board' object that is passed
    # board is an array of 10 strings, excluding index 0, that represents the layout of a board
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    # lets a player decide which symbol they want to be
    # returns an array of both elements to be passed to a variable
  letter = ''
  while not (letter == 'X' or letter == 'O'):
    print('Do you want to be X or O?')
    letter =   input().upper()
  if letter == 'X':
    return ['X','O']
  else:
    return ['O','X']

def whoGoesFirst():
    # randomly choose first player move
  if random.randint(0,1) == 0:
    return 'computer'
  else:
    return 'player'

def playAgain():
    # prompt a user for a replay
  print('Do you want to play again? (yes or no)')
  return   input().lower().startswith('y')

def makeMove(board,letter,move):
    # fills a board at a specific spot with the specified symbol
  board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's symbol, this function returns True if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # top row
    (bo[4] == le and bo[5] == le and bo[6] == le) or # middle row
    (bo[1] == le and bo[2] == le and bo[3] == le) or # bottom row
    (bo[7] == le and bo[4] == le and bo[1] == le) or # left column
    (bo[8] == le and bo[5] == le and bo[2] == le) or # middle column
    (bo[9] == le and bo[6] == le and bo[3] == le) or # right column
    (bo[7] == le and bo[5] == le and bo[3] == le) or # \ diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # / diagonal

def getBoardCopy(board):
    # duplicate a board for the computer to decide
  dupeBoard = []
  for i in board:
    dupeBoard.append(i)
  return dupeBoard

def isSpaceFree(board, move):
    # if index of the board is unoccupied => true
  return board[move] == ' '

def getPlayerMove(board):
    # prompt user for next move
  move = ''
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
    print('What is your next move? (1-9)')
    move =   input()
  return int(move)

def chooseRandomMoveFromList(board, movesList):
    # make a random move
  possibleMoves =[]
  for i in movesList:
    if isSpaceFree(board,i):
      possibleMoves.append(i)
  if len(possibleMoves) != 0:
    return random.choice(possibleMoves)
  else:
    return None

def getComputerMove(board,computerLetter):
    # sets the value for the player's and computer's symbol
  if computerLetter == 'X':
    playerLetter = 'O'
  else:
    playerLetter = 'X'

  for i in range(1,10):
        # loop to see if a winning move can be made; if so, take it
    copy = getBoardCopy(board)
    if isSpaceFree(copy,i):
      makeMove(copy,computerLetter,i)
      if isWinner(copy,computerLetter):
        return i

  for i in range(1,10):
        # loop to see if a player is about to win
    copy = getBoardCopy(board)
    if isSpaceFree(copy,i):
      makeMove(copy,playerLetter,i)
      if isWinner(copy,playerLetter):
                # if the player is about to win, move in that spot
        return i

    # look for a random corner to move into if it is open
  move = chooseRandomMoveFromList(board,[1,3,7,9])
  if move != None:
    return move

    # move into the middle if it is open
  if isSpaceFree(board,5):
    return 5

    # move into a random side spot if it is open
  return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    # check if the board is full
  for i in range(1,10):
    if isSpaceFree(board,i):
      return False
  return True

print('T I C - T A C - T O E')
while True:
  #initialize a board
  theBoard = [' ']*10

  #decide who goes first
  playerLetter, computerLetter = inputPlayerLetter()
  turn = whoGoesFirst()
  print('The ' + turn + ' will go first.')
  
  #keeps the status of the current game
  gameIsPlaying = True

  while gameIsPlaying:
        # run the game until 'gameIsPlaying' is false
        # if the player is first, prompt himm for his move
    if turn == 'player':
      drawBoard(theBoard)
      move = getPlayerMove(theBoard)
      makeMove(theBoard,playerLetter,move)

      if isWinner(theBoard,playerLetter):
                # after every move, check if player has won
                # if they did, congratulate them- if board is full, tie game
                # if neither is the case, it is the computer's turn
        drawBoard(theBoard)
        print('Congratulations! You have won the game!')
        gameIsPlaying = False
      else:
        if isBoardFull(theBoard):
          drawBoard(theBoard)
          print('The game is a tie!')
          break
        else:
          turn = 'computer'

    else:
            # computer's move
      move = getComputerMove(theBoard,computerLetter)
      makeMove(theBoard,computerLetter,move)
      if isWinner(theBoard,computerLetter):
        drawBoard(theBoard)
        print('The computer has won. You lose :(.')
        gameIsPlaying = False
      else:
        if isBoardFull(theBoard):
          drawBoard(theBoard)
          print('The game is tie!')
          break
        else:
          turn = 'player'

  if not playAgain():
    break



