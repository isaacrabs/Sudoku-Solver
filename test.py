class Game:

    def __init__(self, sudoku):
        self.possibleValues = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.sudoku = sudoku

    def solve(self):
        self.notes()
        for row in self.sudoku:
            print(row)

    def getColumn(self, x):
        return [self.sudoku[y][x][0] for y in range(9) if self.sudoku[y][x][0] != ""]

    def getRegion(self, x, y):
        start_x = (x // 3) * 3
        start_y = (y // 3) * 3
        region = []

        for j in range(start_y, start_y + 3):
            for i in range(start_x, start_x + 3):
                value = self.sudoku[j][i][0]
                if value != "":
                    region.append(value)
        return region

    def notes(self):
        for y in range(9):
            for x in range(9):
                cell = self.sudoku[y][x]
                # Check if the cell already has a number (e.g., [5]) or a note
                if len(cell) == 1 and isinstance(cell[0], int):
                    continue

                # Gather constraints
                row = [self.sudoku[y][i][0] for i in range(9) if self.sudoku[y][i][0] != ""]
                col = self.getColumn(x)
                region = self.getRegion(x, y)

                # Start fresh with all values
                pv = self.possibleValues.copy()
                for val in row + col + region:
                    if val in pv:
                        pv.remove(val)

                # Store notes
                self.sudoku[y][x] = [" ".join(pv)]


# Sample empty Sudoku board
sudok = [[[""], [""], [""], [""], [""], [7], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [1], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [6]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [8], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]]]

# Create and solve
sud = Game(sudok)
sud.solve()
