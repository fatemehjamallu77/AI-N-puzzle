from copy import deepcopy
from node import Node
from eight_puzzle import Eight_puzzle
class Bidirectional:
    def __init__(self):
        self.first_frontier = []
        self.first_explored = []
        self.back_frontier = []
        self.back_explored_set = []
        self.goal = None
        self.initial = None
    def get_explored(self):#number of explored nodes
        return len(self.first_explored) + len(self.back_explored_set)
    def creat_goal(self,first,final):
        cur = final.parent
        pre = first
        while cur!=None:
            pre = Node(cur.puzzle,pre,pre.d+1)
            cur = cur.parent
        self.goal = pre
    def solve(self,puzzle):
        if not puzzle.solvable():
            return None
        self.first_frontier.append(Node(puzzle.copy_puzzle()))
        self.initial = puzzle.copy_puzzle()
        self.back_frontier.append(Node(Eight_puzzle(0)))
        if self.first_frontier[0].puzzle.is_goal():
            self.goal = self.first_frontier[0]
            return self.first_frontier[0]
        
        while len(self.first_frontier)!=0:
            cur = self.first_frontier[0]#first in first out(stack)
            del(self.first_frontier[0])
            self.first_explored.append(cur)
            
            for node1 in cur.puzzle.authorized():
                suc = Node(cur.puzzle.copy_puzzle(),cur,cur.d+1)
                suc.puzzle.move(node1)
                if suc.puzzle.is_goal():
                    self.goal = suc
                    return suc
                if not suc in self.first_frontier and not suc in self.first_explored:
                    self.first_frontier.append(suc)
            
            cur = self.back_frontier[0]#first in first out(stack)
            del(self.back_frontier[0])
            self.back_explored_set.append(cur)

            for node2 in cur.puzzle.authorized():
                suc = Node(cur.puzzle.copy_puzzle(),cur)
                suc.puzzle.move(node2)
                if suc.puzzle == self.initial:
                    self.creat_goal(self.initial,suc)
                    return self.goal
                if not suc in self.back_frontier and not suc in self.back_explored_set:
                    self.back_frontier.append(suc)
            

          
            for m in self.first_frontier:#case #1:shared node is in frontiers
                for n in self.back_frontier:
                    if m==n:
                        self.creat_goal(m,n)
                        return self.goal

            for i in self.first_frontier:#case #2:shared node is in forward frontier and backward explored_set
                for j in self.back_explored_set:
                    if i==j:
                        self.creat_goal(i,j)
                        return self.goal

            for s in self.back_frontier:
                for z in self.first_explored:
                    if s==z:
                        self.creat_goal(s,z)
                        return self.goal


        return None
