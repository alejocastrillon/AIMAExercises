from search import *

class missionariesandCannibals(Problem):
    
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.state = initial

    '''Retorna la listas de posibles acciones que se pueden hacer
        en determinado estado para alcanzar el éxito'''
    def actions(self, state):
        if state == (3, 3, 1):
            return ['MC', 'CC']
        elif state == (2, 2, 0):
            return ['M']
        elif state == (3, 1, 0):
            return ['C']
        elif state == (3, 2, 1):
            return ['CC', 'MC']
        elif state == (3, 0, 0):
            return ['C', 'CC']
        elif state == (2, 1, 0):
            return ['M', 'C']
        elif state == (3, 1, 1):
            return ['MM']
        elif state == (2, 2, 1):
            return ['MC', 'MM']
        elif state == (1, 1, 0):
            return ['MC']
        elif state == (0, 2, 0):
            return ['MM', 'C']
        elif state == (0, 3, 1):
            return ['CC']
        elif state == (0, 1, 0):
            return ['C']
        elif state == (0, 2, 1):
            return ['CC']

    '''Retorna la cantidad de misioneros que se deben mover en determinada acción'''
    def quantityMissionariestoMove(self, action):
        a = 0
        for i in action:
            if i == 'M':
                a += 1
        return a

    '''Retorna la cantidad de canibales que se deben mover en determinada acción'''
    def quantityCannibalstoMove(self, action):
        a = 0
        for i in action:
            if i == 'C':
                a += 1
        return a

    '''Dependiendo del lado en donde se encuentre la barca se sumará o restará la cantidad
        de misioneros y canibales, ya que estamos contando la cantidad de misioneros y canibales
        que hay en una margen del río en determinado tiempo'''
    def result(self, state, action):
        qMissionaries = self.quantityMissionariestoMove(action)
        qCannibals = self.quantityCannibalstoMove(action)
        if state[2] == 1:
            return ((state[0] - qMissionaries), (state[1]- qCannibals), 0)
        else:
            return ((state[0] + qMissionaries), (state[1] + qCannibals), 1)

    '''Determina si se ha llegado a un estado exitoso'''
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
    
initial = (3, 3, 1)
goal = (0, 0, 0)
prob = missionariesandCannibals(initial, goal)

s = breadth_first_search(prob)
for node in s.path():
    print(node)