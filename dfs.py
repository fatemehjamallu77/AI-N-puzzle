from copy import deepcopy
from node import Node

def is_in_parents(a,b):#checks if a is already found in b's precedent(inclusive)
    while b!=None:
        if a==b:
            return True
        b = b.parent
    return False

class DFS:
    """
    no explored set was used intentioanlly,because by using it we would fail the advantage of dfs which is
    memory usage of O(md) instead is_in_parents() was used to avoid encountering a same node on a same path
    """
    def __init__(self): 
        self.frontier = []
        self.explored = 0
        self.goal = None
    def get_explored(self):
        return self.explored
    def solve(self,puzzle,d=20):
        if not puzzle.solvable():
            return None
        self.frontier.append(Node(puzzle.copy_puzzle()))
        if self.frontier[0].puzzle.is_goal():
            self.goal = self.frontier[0]
            return self.frontier[0]
        
        while len(self.frontier)!=0:
            cur = self.frontier[-1]
            del(self.frontier[-1])
            self.explored+=1
            
            for node in cur.puzzle.authorized():
                suc = Node(cur.puzzle.copy_puzzle(),cur,cur.d+1)
                suc.puzzle.move(node)
                if suc.puzzle.is_goal():
                    self.goal = suc
                    return suc
                if not suc in self.frontier and not is_in_parents(suc,cur) and suc.d<=d:
                    self.frontier.append(suc)
            

        return None