class Board:
    def __init__(self, m):
        self.m = m
        self.grid = [["." for _ in range(m)] for _ in range(m)]

    def display_board(self):
        board_str = ""
        for i in range(self.m):
            for j in self.grid[i]:
                board_str += f" {j} "
            if i != self.m - 1:
                board_str += "\n"
        return board_str

    def move(self, row, col, mark):
        if self.grid[row][col] != ".":
            return "ERROR"
        else:
            self.grid[row][col] = mark
            return None

    def check_winner(self):
        # Check rows
        for row in self.grid:
            if row.count(row[0]) == self.m and row[0] != ".":
                return f"WINNER {row[0]}"
                
        # Check columns
        for col in range(self.m):
            column = [self.grid[row][col] for row in range(self.m)]
            if column.count(column[0]) == self.m and column[0] != ".":
                return f"WINNER {column[0]}"
                
        # Check main diagonal
        main_diag = [self.grid[i][i] for i in range(self.m)]
        if main_diag.count(main_diag[0]) == self.m and main_diag[0] != ".":
            return f"WINNER {main_diag[0]}"
            
        # Check anti-diagonal
        anti_diag = [self.grid[i][self.m - i - 1] for i in range(self.m)]
        if anti_diag.count(anti_diag[0]) == self.m and anti_diag[0] != ".":
            return f"WINNER {anti_diag[0]}"
            
        # Check if game continues
        for i in range(self.m):
            for j in range(self.m):
                if self.grid[i][j] == ".":
                    return "CONTINUE"
                    
        return "DRAW"

class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark  
        
    def move(self, board: Board, row, col):
        return board.move(row, col, self.mark)

# Example Gameplay
if __name__ == "__main__":
    board = Board(3)
    p1 = Player("Player 1", "X")
    p2 = Player("Player 2", "O")
    
    print("Initial Board:")
    print(board.display_board())
    
    # Simulating moves
    p1.move(board, 0, 0)   
    p2.move(board, 1, 1)  
    p1.move(board, 0, 1)   
    p1.move(board, 0, 2)   
    
    print("\nBoard after moves:")
    print(board.display_board())
    print("\nGame Status:", board.check_winner())