import sys

from logs import Logs



class Game():
    def __init__(self):
        self.board = [
            ['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']
        ]
        self.turn = True
        self.logs = Logs()
        
    def __str__(self):
        return str(self.board)


    def return_board(self):
        return self.board

    def make_move(self, move):
        if self.turn == True:
            self.figure = 'X'
        else:
            self.figure = 'O'
        self.move = move
        
        if self.move < 4:
            self.row = 0
            self.column = self.move - 1 
        elif self.move < 7:
            self.row = 1
            self.column = self.move - 4
        else:
            self.row = 2
            self.column = self.move - 7

        
        if self.board[self.row][self.column] == '*':
            self.board[self.row][self.column] = self.figure
        else: 
            print(f'There is {self.board[self.row][self.column]}')
            return
        player = 'X' if self.turn else 'O'
        self.logs.log_move(player, self.row, self.column, self.board)

        if self.turn == True:
            self.turn = False
        else:
            self.turn = True

        self.show()

    def check(self):
        for i in range(3):
            
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '*':
                self.logs.download_logs()
                return self.board[i][0]

            
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '*':
                self.logs.download_logs()
                return self.board[0][i]


        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != '*') or \
        (self.board[0][2] == self.board[1][1] == self.board[2][0] != '*'):
            self.logs.download_logs()
            return self.board[1][1]
        

        draw = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X' or self.board[i][j] == 'O':
                    pass
                else:
                    draw = False

        if draw == True:
            self.logs.download_logs()
            print("It's draw!")
            return "It's draw!"
        return None



   
            

                
                
        






    def show(self):

        print('\n'.join([' | ' + ' | '.join(row) + ' | ' for row in self.board]))   
        self.check()  
        


         
        

