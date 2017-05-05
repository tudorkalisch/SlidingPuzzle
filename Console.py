from Controller import  Controller
class Console:
    def __init__(self):
        self.cont = Controller()

    def printMenu(self):
        print("Menu:")
        print("1 - BFS")

        print("x - Exit")

    def mainMenu(self):
        prob = self.cont.getProblem()
        prob.printInitialState()
        prob.printFinalState()
        cond = 0

        while cond != "x":
            self.printMenu()
            cond = input("Input: ")
            if cond == "1":
                prob.solveBfs(prob.initialState, prob.finalState)
            if cond == "x":
                break

    def solve(self):
        self.cont.getProblem().solveBfs()