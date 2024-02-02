class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # 3 x 3 grid
        n = 3
        empty_square = (n * n) - len(moves)
        # rows and columns
        rows, cols = [0] * n, [0] * n
        # diagonals
        primary_diagonal = 0
        secondary_diagonal = 0

        for i in range(len(moves)):
            x, y = moves[i]
            
            # player A
            if i % 2 == 0:
                mark = 1
            else: # player B
                mark = -1
            rows[x] += mark
            cols[y] += mark

            if x == y:
                primary_diagonal += mark
            if x + y == n - 1:
                secondary_diagonal += mark

            # check if there is same mark in a row
            if abs(rows[x]) == n or abs(cols[y]) == n or abs(primary_diagonal) == n or abs(secondary_diagonal) == n:
                if mark == 1:
                    return 'A'
                else:
                    return 'B'

        if empty_square == 0:
            return 'Draw'

        return 'Pending'