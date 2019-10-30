
class TaTeTi():

    def __init__(self,board = None):
        if not board:
            board = [' ' for _ in range(9)]
        self.board = board

    def full(self):
        for value in self.board:
            if value == ' ': 
                return False
        return True
    
    def win(self):
        if self.board[0] != " " and self.board[0]==self.board[4] and self.board[4]==self.board[8]:
            return True
        if self.board[2]!= " " and self.board[2]==self.board[4] and self.board[4]==self.board[6]:
            return True
        if self.board[0]!= " " and self.board[0]==self.board[3] and self.board[3]==self.board[6]:
            return True
        if self.board[1]!= " " and self.board[1]==self.board[4] and self.board[4]==self.board[7]:
            return True
        if self.board[2]!= " " and self.board[2]==self.board[5] and self.board[5]==self.board[8]:
            return True
        if self.board[0]!= " " and self.board[0]==self.board[1] and self.board[1]==self.board[2]:
            return True
        if self.board[3]!= " " and self.board[3]==self.board[4] and self.board[4]==self.board[5]:
            return True
        if self.board[6]!= " " and self.board[6]==self.board[7] and self.board[7]==self.board[8]:
            return True
        return False
    

    def validate(self,posicion):
        if self.board[posicion-1] != ' ':
            return False
        return True
    
    def assign(self,posicion,piece):

        if self.validate(posicion):
            self.board[posicion-1] = piece

        elif self.validate(posicion) is False:
            raise Exception
        
    def draw_board(self):
        self.monitor = "\n"
        for i in range(9):
            if self.board[i] != " ":
                self.monitor += " " + self.board[i] + " "
            else:
                self.monitor += " " + str(i+1) + " "
            if i == 2 or i == 5:
                self.monitor += "\n---+---+---\n"
            elif i == 8:
                self.monitor += "\n"
            else:
                self.monitor += "|"

        return self.monitor  

if __name__ == "__main__":
    u = TaTeTi()
    u.play()