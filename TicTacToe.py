import sys

board = [['-', '-', '-'], 
         ['-', '-', '-'], 
         ['-', '-', '-']] #improve layout
playerX = input('Player X. Please type in your name: ')
playerO = input('Player O. Please type in your name: ')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = []
board_list = {1: board[0][0], 2: board[0][1], 3: board[0][2], 4: board[1][0], 5: board[1][1], 6: board[1][2], 7: board[2][0], 8: board[2][1], 9: board[2][2]}


def diagonal():
        if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
                return True
        elif(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
                return True

def print_board():
        for i in board:
                print(' '.join(i))
        print()

def horizontal():
        for i in board:
                count2 = 0
                count3 = 0
                for j in i:
                        if j == 'X':
                                count2 += 1
                        if j == 'O':
                                count3 += 1
                if (count2 == 3 or count3 == 3):
                        return True
                


#function wrong
def vertical():
        for i, v in enumerate(board[0]):
                if v == 'X':
                        if ((board[1][i]) == 'X' and (board[2][i]) == 'X'):
                                return True
                elif v == 'O':
                        if ((board[1][i]) == 'O' and (board[2][i]) == 'O'):
                                return True


          


def result():
        if (diagonal() == True or horizontal() == True or vertical() == True):
                print('We have a winner!')
                sys.exit()



 


for i in range(8):
        xinput = int(input(f'{playerX} please pick a number from 1-9: '))
        if (xinput in list) and (xinput not in list1):
                row = (xinput - 1) // 3
                col = (xinput - 1) % 3
                board[row][col] = 'X'         
                list1.append(xinput)
                print_board()  #update board after input
                result() 
        oinput = int(input(f'{playerO} please pick a number from 1-9: '))
        if (oinput in list) and (oinput not in list1):
                row1 = (oinput - 1) // 3
                col1 = (oinput - 1) % 3
                board[row1][col1] = 'O'
                list1.append(oinput)
                print_board()
                result()

print('Its a Tie!')


    
