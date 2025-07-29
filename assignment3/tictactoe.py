class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board():

    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]    
    
    def __init__(self):
        self.board_array = [[" " for i in range (3)] for j in range(3)]
        self.turn = "X"
    
    def __str__(self):
        board = []
        for row in self.board_array:
            line="|".join(row)
            board.append(line)
            board.append("-"*len(line))
        return "\n".join(board[:-1])   

    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")
            
board = Board()
print("The Tic Tac Toe game has begun!\n")
print (board)

while True:
    print(f"Time for {board.turn}")
    pl_input=input("Enter your move, please ")

    try:
        board.move(pl_input)
    except TictactoeException as e:
        print(e.message)
        continue

    print(board)

    game_over, message= board.whats_next()
    if game_over:
        print("\n"+message)
        break

