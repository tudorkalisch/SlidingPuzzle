from Problem import Problem
class Controller():
    def __init__(self):
        self.problem = Problem()

    def printState(self):
        self.problem.printState();

    def getProblem(self):
        return self.problem