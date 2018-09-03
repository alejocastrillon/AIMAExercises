from search import *
import math
import random

class TSP(Problem):
    def __init__(self, initial):
        Problem.__init__(self, initial, None)
        self.state = initial
    
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

    def actions(self, state):
        return ['CH']

    def distanceTotal(self, state):
        distance = 0;
        for i in range(0, len(state)):
            if i == (len(state) - 1):
                distance += math.sqrt(math.pow((state[i][0] - state[0][0]), 2) + math.pow((state[i][1] - state[0][1]), 2))
            else:
                distance += math.sqrt(math.pow((state[i][0] - state[i + 1][0]), 2) + math.pow((state[i][1] - state[i + 1][1]), 2))
        return distance

    def changeOrderCities(self, state):
        pos1 = random.randint(0, (len(state) - 1))
        pos2 = random.randint(0, (len(state) - 1))
        resultState = self.convertStateintoList(state)
        data = resultState[pos1]
        resultState[pos1] = resultState[pos2]
        resultState[pos2] = data
        return resultState

    def result(self, state, action):
        if action == 'CH':
            return self.convertStateintoTuple(self.changeOrderCities(state))

    
    def goal_test(self, state):
        return self.distanceTotal(state) < self.distanceTotal(self.initial)

    def h(self, node):
        return self.distanceTotal(node.state)


initial = ((235, 143), (509, 347), (657, 345), (132,120))

def distanceTotal(state):
    distance = 0;
    for i in range(0, len(state)):
        if i == (len(state) - 1):
            distance += math.sqrt(math.pow((state[i][0] - state[0][0]), 2) + math.pow((state[i][1] - state[0][1]), 2))
        else:
            distance += math.sqrt(math.pow((state[i][0] - state[i + 1][0]), 2) + math.pow((state[i][1] - state[i + 1][1]), 2))
    return distance

tsp = TSP(initial)
t = astar_search(tsp)
for node in t.path():
    print(node)
    print("Distancia: ", distanceTotal(node.state))