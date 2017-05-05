import copy
class Node:
    def __init__(self,_givenMatrix):
        self.matrix = _givenMatrix
        self.children = []

    def findEmpty(self):
        for i in range (0,len(self.matrix)):
            for j in range (0,len(self.matrix)):
                if(self.matrix[i][j] == 0):
                    result = []
                    result.append(i)
                    result.append(j)
                    return result
    def getMatrix(self):
        return self.matrix
    def possibleMoves(self):
        positionEmpty = self.findEmpty()
        possibleMoves = ["U","D","L","R"]
        if positionEmpty[0] == 0:
            possibleMoves.remove("U")
        if positionEmpty[0] == len(self.matrix)-1:
            possibleMoves.remove("D")
        if positionEmpty[1] == 0:
            possibleMoves.remove("L")
        if positionEmpty[1] == len(self.matrix)-1:
            possibleMoves.remove("R")
        return possibleMoves
    def MoveUp(self):
        postionEmpty = self.findEmpty()
        row = postionEmpty[0]
        column = postionEmpty[1]
        auxMatrix = copy.deepcopy(self.getMatrix())
        auxMatrix[row-1][column],auxMatrix[row][column] = auxMatrix[row][column],auxMatrix[row-1][column]
        return auxMatrix
    def MoveDown(self):
        postionEmpty = self.findEmpty()
        row = postionEmpty[0]
        column = postionEmpty[1]
        auxMatrix = copy.deepcopy(self.getMatrix())
        auxMatrix[row+1][column],auxMatrix[row][column] = auxMatrix[row][column],auxMatrix[row+1][column]
        return auxMatrix
    def MoveRight(self):
        postionEmpty = self.findEmpty()
        row = postionEmpty[0]
        column = postionEmpty[1]
        auxMatrix = copy.deepcopy(self.getMatrix())
        auxMatrix[row][column+1],auxMatrix[row][column] = auxMatrix[row][column],auxMatrix[row][column+1]
        return auxMatrix
    def MoveLeft(self):
        postionEmpty = self.findEmpty()
        row = postionEmpty[0]
        column = postionEmpty[1]
        auxMatrix = copy.deepcopy(self.getMatrix())
        auxMatrix[row][column-1],auxMatrix[row][column] = auxMatrix[row][column],auxMatrix[row][column-1]
        return auxMatrix
    def expand(self):
        possibleMoves = self.possibleMoves()
        for i in possibleMoves:
            if i == "U":
                self.children.append(self.MoveUp())
            if i == "D":
                self.children.append(self.MoveDown())
            if i == "R":
                self.children.append(self.MoveRight())
            if i == "L":
                self.children.append(self.MoveLeft())
        return self.children

    def __eq__(self, other):
        return self.matrix == other
    def __str__(self):
        string = "Board:\n"
        for i in self.matrix:
            string += str(i)
            string += "\n"
        return string


