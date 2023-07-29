
from node import Node
from copy import deepcopy

class BFS:
    def __init__(self):
        self.frontier = []
        self.explored_set = []
        self.goal = None
    def get_explored(self):
        return len(self.explored_set)
    def solve(self,puzzle):
        if not puzzle.solvable():
            return None
        self.frontier.append(Node(puzzle.copy_puzzle()))
        if self.frontier[0].puzzle.is_goal():
            self.goal = self.frontier[0]
            return self.frontier[0]
        
        while len(self.frontier)!=0:
            cur = self.frontier[0]
            del(self.frontier[0])
            self.explored_set.append(cur)
            
            for node in cur.puzzle.authorized():
                suc = Node(cur.puzzle.copy_puzzle(),cur,cur.d+1)
                print(suc.d)
                suc.puzzle.move(node)
                if suc.puzzle.is_goal():
                    self.goal = suc
                    return suc
                if not suc in self.frontier and not suc in self.explored_set:
                    self.frontier.append(suc)
            

        return None

