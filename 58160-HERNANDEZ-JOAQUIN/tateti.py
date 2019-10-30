
class TaTeTi():

    def __init__(self,board=None):
            if not board:
                board = [' ' for _ in range(9)]
            self.board = board

    def full (self):
        board2 = 0
        for j in range(9):
            if self.board[j] != ' ':
                board2 += 1
        if board2 == 9:
            return True
        else:
            return False

    def win(self):

        if self.board[0]!= " " and self.board[0]==self.board[3] and self.board[3]==self.board[6]:
            return True

        if self.board[1]!= " " and self.board[1]==self.board[4] and self.board[4]==self.board[7]:
            return True

        if self.board[2]!= " " and self.board[2]==self.board[5] and self.board[5]==self.board[8]:
            return True

        if self.board[0]!= " " and self.board[0]==self.board[1] and self.board[1]==self.board[2]:
            return True

        if self.board[0] != " " and self.board[0]==self.board[4] and self.board[4]==self.board[8]:
            return True

        if self.board[2]!= " " and self.board[2]==self.board[4] and self.board[4]==self.board[6]:
            return True

        if self.board[3]!= " " and self.board[3]==self.board[4] and self.board[4]==self.board[5]:
            return True

        if self.board[6]!= " " and self.board[6]==self.board[7] and self.board[7]==self.board[8]:
            return True
        return False

    
    def validate(self, position):
        if self.board[position-1] == " ":
           return True
    
    def assign(self,position,pieza):
        if not (self.validate(position)):
           raise Exception
        else:
           self.board[position-1]=pieza

    def draw_board(self):

        self.display = "\n"
        for numero in range(9):
           if self.board[numero] != " ":
               self.display += " " + self.board[numero] + " "
           else:
               self.display += " " + str(1+numero) + " "
           if numero == 2 or numero == 5:
               self.display += "\n---+---+---\n"
           elif numero == 8:
               self.display += "\n"
           else:
               self.display += "|"        
        return self.display

    

