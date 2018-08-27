from search import *
import os

class puzzle(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.state = initial

    '''Retorna las coordenadas del espacio
    representado en la matriz por 0'''
    def positionWhite(self, state):
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i][j] == 0:
                    return (i, j)

    '''Se determinan las posibles acciones de acuerdo
    a la posicion del espacio'''
    def actions(self, state):
        pos = self.positionWhite(state)
        if pos[0] == 0 and pos[1] == 0:
            return ['MB', 'MD']
        elif pos[0] == 0 and pos[1] == 2:
            return ['MB', 'MI']     
        elif pos[0] == 0:
            return ['MB', 'MI', 'MD']
        elif pos[0] == 2 and pos[1] == 0:
            return ['MA', 'MD']
        elif pos[0] == 2 and pos[1] == 2:
            return ['MA', 'MI']
        elif pos[0] == 2:
            return ['MA', 'MI', 'MD']
        elif pos[1] == 0:
            return ['MA', 'MB', 'MD']
        elif pos[1] == 2:
            return ['MA', 'MB', 'MI']
        else:
            return ['MA', 'MB', 'MI', 'MD']

    '''Convierte la matriz de tuplas en una lista de lista
    para permitir su modificacion'''
    def convertStateintoList(self, state):
        tList = []
        for x in state:
            tList.append(list(x))
        return tList

    '''Convierte la lista de lista en una matriz de tuplas
    para el metodo breadth_first_search'''
    def convertStateintoTuple(self, liststate):
        tTuple =[]
        for x in liststate:
            tTuple.append(tuple(x))
        return tuple(tTuple)

    def messageProcessing(self):
        for i in range(1, 5):
            tr = '.' * i
            print("Processing",  tr)
            os.system('clear')


    '''Dependiendo del estado y la accion se mueven los cuadros'''
    def result(self, state, action):
        pos = self.positionWhite(state)
        t = self.convertStateintoList(state)
        '''print(pos)
        print(t)'''
        #self.messageProcessing()
        if action == 'MA':
            p = t[pos[0] - 1][pos[1]]
            t[pos[0]][pos[1]] = p
            t[pos[0] - 1][pos[1]] = 0
        elif action == 'MB':
            p = t[pos[0] + 1][pos[1]]
            t[pos[0]][pos[1]] = p
            t[pos[0] + 1][pos[1]] = 0
        elif action == 'MI':
            p = t[pos[0]][pos[1] - 1]
            t[pos[0]][pos[1]] = p
            t[pos[0]][pos[1] - 1] = 0
        elif action == 'MD':
            p = t[pos[0]][pos[1] + 1]
            t[pos[0]][pos[1]] = p
            t[pos[0]][pos[1] + 1] = 0
        
        return self.convertStateintoTuple(t)
    
    def goal_test(self, state):
        return True if state == self.goal else False

def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

def depth_first_graph_search(problem):
    """Search the deepest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Does not get trapped by loops.
        If two paths reach a state, only use the first one. [Figure 3.7]"""
    frontier = [(Node(problem.initial))]  # Stack
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)
    return None

'''Este ejemplo es sencillo, lo coloque porque es uno de los que toma menos tiempo de realizar'''
initial = ((4, 1, 2), (7, 0, 3), (8, 5, 6))
goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
puz = puzzle(initial, goal)

s = breadth_first_search(puz)
for node in s.path():
    print(node)