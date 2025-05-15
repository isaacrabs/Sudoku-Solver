class Game:

    def __init__(self, sudoku):
        self.availableNumbers = {'1': 0,
                                 '2': 0,
                                 '3': 0,
                                 '4': 0,
                                 '5': 0,
                                 '6': 0,
                                 '7': 0,
                                 '8': 0,
                                 '9': 0}

        self.possibleValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.sudoku = sudoku

    def solve(self):
        iteration = 0
        self.notes()
        print(self.sudoku)

    def getColumn(self, position):
        column = []
        for record in self.sudoku:
            column.append(record[position])

        return column

    def getRegion(self, xposition, yposition):
        region = []
        newSud = self.sudoku

        if yposition in [0, 1, 2]:
            for i in range(3):
                region.append(newSud[i])

        elif yposition in [3, 4, 5]:
            for i in range(3, 6):
                region.append(newSud[i])

        elif yposition in [6, 7, 8]:
            for i in range(6, 9):
                region.append(i)

        if xposition in [0, 1, 2]:
            for row in region:
                for i in range(6):
                    row.pop(3)

        elif xposition in [3, 4, 5]:
            for row in region:
                for i in range(3):
                    row.pop(0)

                for i in range(3):
                    row.pop(3)

        elif xposition in [6, 7, 8]:
            for row in region:
                for i in range(6):
                    row.pop(0)

        return region

    def notes(self):
        for y in range(0, 9):
            row = self.sudoku[y]
            for x in range(0, 9):
                cell = row[x]
                if type(cell[0]) == int:
                    pass
                else:
                    column = self.getColumn(x)
                    region = self.getRegion(x, y)
                    pv = self.possibleValues
                    for i in range(1, 10):
                        if i in column or i in row or i in region[0] or i in region[1] or i in region[2]:
                            pv.remove(i)

                    possibles = " ".join(pv)
                    self.sudoku[x][y] = possibles


sudok = [[[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""], [""]]]

sud = Game(sudok)
sud.solve()
