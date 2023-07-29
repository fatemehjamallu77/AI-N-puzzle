from random import *
import copy

class Eight_puzzle:
    def __init__(self,n=100):#create puzzle and shuffle table n times from the goal state
        self.table = [[1,2,3],[4,5,6],[7,8,0]]
        for i in range(n):
            actions = self.authorized()
            action=choice(actions)
            self.move(action)

    def __eq__(self,rhs):#checks if tables are identical
        return self.table==rhs.table


    def authorized(self):#get legal actions
        result = []
        sign = False
        for n in range(3):
            if sign:
                break
            for m in range(3):
                if self.table[n][m]==0:#finds the 0 tile
                    x,y = n,m
                    sign = True
                    break
        
        for sum in [(-1,0),(0,-1),(0,1),(1,0)]:#for adjacent tiles
            if x+sum[0]>=0 and x+sum[0]<3 and y+sum[1]>=0 and y+sum[1]<3:#checks for boundries
                result.append((x+sum[0],y+sum[1]))
        return result


    def is_goal(self):#checks if we reached the goal state
        return self.table == [[1,2,3],[4,5,6],[7,8,0]]

    

    def move(self,action):#if action is legal it applies to table
        x,y = action[0],action[1]
        if self.table[x][y]!=0:
            x2,y2 = None,None
            for sum in [(-1,0),(0,-1),(0,1),(1,0)]:
                if x+sum[0]>=0 and x+sum[0]<3 and y+sum[1]>=0 and y+sum[1]<3 and self.table[x+sum[0]][y+sum[1]]==0:
                    x2,y2 = x+sum[0],y+sum[1]
                    break
            
            if x2!= None and y2!=None:
                self.table[x][y],self.table[x2][y2] = self.table[x2][y2],self.table[x][y]
            
                
            

    def copy_puzzle(self):#returns a new instance of puzzle with an identical table
        puzzle_copy = Eight_puzzle(0)
        puzzle_copy.table = self.copy_table()
        return puzzle_copy
    def copy_table(self):
        return copy.deepcopy(self.table)


                    
    def print_table(self):
        print("current position(state)  :")
        for i in range(3):
            for j in range(3):                
                print(self.table[i][j],end=' ')
            print('')
    


    def solvable(self):
        inversions = 0
        for i in range(9):
            for j in range(i+1,9):
                if self.table[i//3][i%3]==0 or self.table[j//3][j%3]==0:
                    continue
                if self.table[i//3][i%3]>self.table[j//3][j%3]:
                    inversions+=1
        if inversions%2==0:
            return True
        else:
            return False


