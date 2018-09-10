from search import *
import random

class Horses(Problem):
    
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.state = initial
        self.numberHorse = 0

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

    def validateMove(self, state, direction):
        cont = 0
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i][j] == 1 or state[i][j] == 2:
                    cont += 1
                    if cont == self.numberHorse:
                        #2 espacios en el eje y sentido positivo y 1 espacio en el eje x sentido negativo
                        if direction == 'M1':
                            if ((i - 2) <  0 and (j - 1) < 0):
                                return False
                            elif (state[i - 2][j - 1] == 1 or state[i - 2][j - 1] == 2):
                                return False
                            else:
                                return True
                        #2 espacios en el eje y sentido postivo y 1 espacio en el eje x sentido positivo
                        elif direction == 'M2':
                            if ((i - 2) <  0 and (j + 1) > 2):
                                return False
                            elif (state[i - 2][j + 1] == 1 or state[i - 2][j + 1] == 2):
                                return False
                            else:
                                return True
                        #2 espacios en el eje y sentido negativo y 1 espacio en el eje x sentido negativo
                        elif direction == 'M3':
                            if ((i + 2) > 2 and (j - 1) < 0):
                                return False
                            elif (state[i + 2][j - 1] == 1 or state[i + 2][j - 1] == 2):
                                return False
                            else:
                                return True
                        #2 espacios en el eje y sentido negativo y 1 espacio en el eje x sentido positivo
                        elif direction == 'M4':
                            if ((i + 2) > 2 and (j + 1) > 2):
                                return False
                            elif (state[i + 2][j + 1] == 1 or state[i + 2][j + 1] == 2):
                                return False
                            else:
                                return True
                        #1 espacio en el eje y sentido positivo y 2 espacios en el eje x sentido negativo
                        elif direction == 'M5':
                            if ((i - 1) < 0 and (j - 2) < 0):
                                return False
                            elif  (state[i - 1][j - 2] == 1 or state[i - 1][j - 2] == 2):
                                return False
                            else:
                                return True
                        #1 espacio en el eje y sentido positivo y 2 espacios en el eje x sentido positivo
                        elif direction == 'M6':
                            if ((i - 1) < 0 and (j + 2) > 2):
                                return False
                            elif (state[i - 1][j + 2] == 1 or state[i - 1][j + 2] == 2):
                                return False
                            else:
                                return True
                        #1 espacio en el eje y sentido negativo y 2 espacios en el eje x sentido negativo
                        elif direction == 'M7':
                            if ((i + 1) > 2 and (j - 2) < 0):
                                return False
                            elif (state[i + 1][j - 2] == 1 or state[i + 1][j - 2] == 2):
                                return False
                            else:
                                return True
                        #1 espacio en el eje y sentido negativo y 2 espacios en el eje x sentido positivo
                        elif direction == 'M8':
                            if ((i + 1) > 2 and (j + 2) > 2):
                                return False
                            elif  (state[i + 1][j + 2] == 1 or state[i + 1][j + 2] == 2):
                                return False
                            else:
                                return True

    def makeChange(self, state, direction):
        resultState = self.convertStateintoList(state)
        cont = 0
        for i in range(0, len(resultState)):
            for j in range(0, len(resultState[i])):
                if state[i][j] == 1 or state[i][j] == 2:
                    cont += 1
                    if self.numberHorse == cont:
                        data = resultState[i][j]
                        if direction == 'M1':
                            resultState[i][j] = 0
                            resultState[i - 2][j - 1] = data
                            return self.convertStateintoTuple(resultState)
                        elif direction == 'M2':
                            resultState[i][j] = 0
                            resultState[i - 2][j + 1] = data
                            return self.convertStateintoTuple(resultState)
                        elif direction == 'M3':
                            resultState[i][j] = 0
                            resultState[i + 2][j - 1] = data
                            return self.convertStateintoTuple(resultState)
                        elif direction == 'M4':
                            resultState[i][j] = 0
                            resultState[i + 2][j + 1] = data
                            return self.convertStateintoTuple(resultState)
                        elif direction == 'M5':
                            resultState[i][j] = 0
                            resultState[i - 1][j - 2] = data
                            return self.convertStateintoTuple(resultState)
                        elif direction == 'M6':
                            resultState[i][j] = 0
                            resultState[i - 1][j + 2] = data
                            return self.convertStateintoTuple(resultState)
                        elif direction == 'M7':
                            resultState[i][j] = 0
                            resultState[i + 1][j - 2] = data
                            return self.convertStateintoTuple(resultState)
                        elif direction == 'M8':
                            resultState[i][j] = 0
                            resultState[i + 1][j + 2] = data
                            return self.convertStateintoTuple(resultState)

    def coordHorsetoMove(self, state):
        cont = 0
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i][j] == 1 or state[i][j] == 2:
                    cont += 1
                    if cont == self.numberHorse:
                        return (i, j)

    def actions(self, state):
        if self.numberHorse >= 4:
            self.numberHorse = 0
        self.numberHorse += 1
        print(self.numberHorse)
        pos = self.coordHorsetoMove(state)
        print(pos)
        print(state)
        if pos[0] == 0:
            if pos[1] == 0:
                return ['M8', 'M4']
            elif pos[1] == 1:
                return ['M4', 'M3']
            elif pos[1] == 2:
                return ['M7', 'M3']
        elif pos[0] == 1:
            if pos[1] == 0:
                return ['M6', 'M8']
            elif pos[1] == 1:
                return ['M5', 'M7']
        elif pos[0] == 2:
            if pos[1] == 0:
                return ['M2', 'M6']
            elif pos[1] == 1:
                return ['M1', 'M2']
            elif pos[1] == 2:
                return ['M1', 'M5']
            


    def result(self, state, action):
        if self.validateMove(state, action):
            return self.makeChange(state, action)

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

initial = ((1, 0, 1), (0, 0, 0), (2, 0, 2))
goal = ((2, 0, 2), (0, 0, 0), (1, 0, 1))

horse = Horses(initial, goal)

s = breadth_first_search(horse)

for node in s.path():
    print(node)