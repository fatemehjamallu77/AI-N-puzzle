from eight_puzzle import Eight_puzzle
from bfs import BFS
from dfs import DFS
from bidirectional import Bidirectional
import time
start_time = time.time()
end_time=0


def solvable():  # barresi mikonad aya ghabele hale
  priority = 0
  for i in range(9):
    for j in range(i + 1, 9):
      if initial.table[i // 3][i % 3] == 0 or initial.table[j // 3][j % 3] == 0:
        continue
      if  initial.table[i // 3][i % 3] > initial.table[j // 3][j % 3]:
        priority += 1
  if priority % 2 == 0:
    return True
  else:
    return False

initial = Eight_puzzle(30)
initial.table = [[8,6,7],[2,5,4],[3,0,1]]#table mitoone besoorate dasti tanzim she
print(' initial state of 8_puzzle :')
initial.print_table()
print('')
solution2 = DFS()
solution1 = BFS()
solution3 = Bidirectional()

bfs1 = solution1.solve(initial)
dfs2 = solution2.solve(initial)
bidirectional3 = solution3.solve(initial)




if solvable():
  if bfs1!=None :
    print('1 explored_set:',solution1.get_explored())
    print('1 DEPTH:',bfs1.d)
    print('1 BFS:')
    bfs1.print_path()
    end_time=time.time()
    print("--- %s seconds is this runtime ---" % (end_time - start_time))
    end_time=0

  if dfs2!=None:
    print('2 explored_set:',solution2.get_explored())
    print('2 DEPTH:',dfs2.d)
    print('2 DFS:')
    dfs2.print_path()
    end_time=time.time()
    print("--- %s seconds is this runtime ---" % (end_time - start_time))
    end_time=0    
  if bidirectional3!=None:
    print('3 explored_set',solution3.get_explored())
    print('3 DEPTH',bidirectional3.d)
    print('3 Bidirectional:')
    bidirectional3.print_path()
    end_time=time.time()
    print("--- %s seconds is this runtime ---" % (end_time - start_time))
    end_time=0    
        
    
else :
    print(" ERRORE: ( not solvable)" )