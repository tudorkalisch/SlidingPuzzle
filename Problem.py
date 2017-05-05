from Node import Node
class Problem:
    def __init__(self):
        self.initialState = []
        self.finalState = []
        self.visited = []
        self.dimension = 0
        self.readFromFile()

    def solveBfs(self, root, el):
        tovisit = []
        el = Node(self.finalState)
        root = Node(self.initialState)
        tovisit.append(root)
        visited = []
        found = False
        nr = 1
        while len(tovisit) != 0 and not found:
            node = tovisit.pop()

            print(str(nr) + " " + str(node))
            nr += 1
            if node.__eq__(el):
                found = True
            else:
                visited.append(node.getMatrix())
                aux = node.expand()
                children = []
                for x in aux:
                    newnode = Node(x)
                    if newnode.getMatrix() not in visited:
                        children.append(newnode)
                tovisit = tovisit + children
        if found == True:
            print("Success")
        return found
    def inVisited(self,node):
        for x in self.visited:
            if node.__eq__(x):
                return True
        return False

    def readFromFile(self):
        aux = []
        file = open("InputFile.txt", "r")
        self.dimension = int(file.readline());

        for i in range(0, self.dimension):
            lines = file.readline()
            data = []
            for d in lines.split():
                data.append(int(d))
            self.initialState.append(data)

        for i in range(0, self.dimension):
            lines = file.readline()
            data = []
            for d in lines.split():
                data.append(int(d))
            self.finalState.append(data)

    def printInitialState(self):
        print("Initial State")
        for i in self.initialState:
            print(i)
        print()

    def printFinalState(self):
        print("Final State")
        for i in self.finalState:
            print(i)
        print()
