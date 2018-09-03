from search import *
import os
import math

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

    '''Retorna las coordenadas de un numero
    en un estado'''
    def positionNumber(self, state, number):
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i][j] == number:
                    return (i, j)

    def quantityStateinBestPos(self, state):
        cont = 0
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i][j] == self.goal[i][j]:
                    cont += 1
        return cont

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

    def quantityElementsinWrongPosition(self, state):
        cont = 0
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i][j] != self.goal[i][j]:
                    cont += 1
        return cont

    def quantityMovestoBestPosition(self, state, number):
        cont = 0
        actualPosition = list(self.positionNumber(state, number))
        exitoPosition = list(self.positionNumber(self.goal, number))
        while actualPosition[0] != exitoPosition[0]:
            if actualPosition[0] > exitoPosition[0]:
                actualPosition[0] -= 1
            else:
                actualPosition[0] += 1
            cont += 1
        while actualPosition[1] != exitoPosition[1]:
            if actualPosition[1] > exitoPosition[1]:
                actualPosition[1] -= 1
            else:
                actualPosition[1] += 1
            cont += 1
        return cont

    def h(self, node):
        distancia = 0
        #Prioridad Hamming
        #return self.quantityElementsinWrongPosition(node.state)
        #Manhattan
        for i in range(0, 9):
            distancia += self.quantityMovestoBestPosition(node.state, i)
        #Distancia Euclidiana
        '''for i in range(0, 9):
            coordenadaEstado = self.positionNumber(node.state, i)
            coordenadaExito = self.positionNumber(self.goal, i)
            distancia += math.sqrt(math.pow((coordenadaEstado[0] - coordenadaExito[0]), 2) + math.pow((coordenadaEstado[1] - coordenadaExito[1]), 2))'''
        #Distancia Chebyshov
        '''for i in range(0, 9):
            coordenadaEstado = self.positionNumber(node.state, i)
            coordenadaExito = self.positionNumber(self.goal, i)
            distancia += max(math.fabs(coordenadaEstado[0] - coordenadaExito[0]), math.fabs(coordenadaEstado[1] - coordenadaExito[1]))'''
        #Distancia Jaccard
        #distancia = self.quantityStateinBestPos(node.state) / 18
        #Distancia Canberra
        '''for i in range(0, 9):
            coordenadaEstado = self.positionNumber(node.state, i)
            coordenadaExito = self.positionNumber(self.goal, i)
            magnitud_diferencia = math.sqrt(math.pow((coordenadaEstado[0] - coordenadaExito[0]), 2) + math.pow((coordenadaEstado[1] - coordenadaExito[1]), 2))
            magnitud_estado = math.sqrt(math.pow(coordenadaEstado[0], 2) + math.pow(coordenadaEstado[1], 2))
            magnitud_exito = math.sqrt(math.pow(coordenadaExito[0], 2) + math.pow(coordenadaExito[1], 2))
            if (magnitud_estado + magnitud_exito) != 0:
                 distancia += magnitud_diferencia / (magnitud_estado + magnitud_exito)'''
        print(distancia)
        return distancia

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
#initial = ((4, 0, 2), (7, 1, 3), (8, 5, 6))
initial = ((7, 4, 2), (1, 3, 0), (8, 5, 6))
#initial = ((4, 2, 0), (7, 1, 6), (8, 5, 3))
goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
puz = puzzle(initial, goal)

s = astar_search(puz)
#s = uniform_cost_search(puz)
for node in s.path():
    print(node)