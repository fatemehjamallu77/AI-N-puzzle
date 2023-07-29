from eight_puzzle import Eight_puzzle

class Node:
    def __init__(self,puzzle,parent=None,d=0):
        self.puzzle = puzzle
        self.parent = parent
        self.d = d
    def __eq__(self,rhs):#two nodes are compared with their current state(puzzle)
        if rhs==None:
            return False
        return self.puzzle == rhs.puzzle

    def reversing_path(self):
        self.puzzle.print_table()
        if type(self.parent) != type(None):
            self.parent.print_path()
        print('')
    

    def print_path(self):#prints the path recursively from parents to current node
        if type(self.parent) != type(None):
            self.parent.print_path()
        self.puzzle.print_table()
        print('')

'''    def manhattanDistance(self):
        result = 0
        count = 1
        for i in range(3):
            for j in range(3):
                index = self.puzzle[i][j] - 1
                distance = (2-i)+(2-j) if index == -1 else abs(i-(index/3))+abs(j-(index%3))
                result += distance
                count+=1
        return result'''