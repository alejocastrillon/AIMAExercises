from simpleai.search import SearchProblem, astar
import pygame

INITIAL = ((4, 1, 2), (7, 0, 3), (8, 5, 6))
GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
class Puzzle(SearchProblem):

    '''Retorna las coordenadas del espacio
    representado en la matriz por 0'''
    def positionWhite(self, state):
        for i in range(0, len(state)):
            for j in range(0, len(state[i])):
                if state[i][j] == 0:
                    return (i, j)

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
    para permitir su modificación'''
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

    def result(self, state, action):
        pos = self.positionWhite(state)
        t = self.convertStateintoList(state)
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

    def is_goal(self, state):
        return state == GOAL
    
size = width, height = [800, 600]
pygame.init()
pantalla = pygame.display.set_mode(size)
p = Puzzle()
result = astar(Puzzle(INITIAL))
resultado = result.path()
print(resultado)
done = False
interactive = False
while not done:
    font = pygame.font.Font('freesansbold.ttf',20)
    if not interactive:
        for action, state in resultado:
            y = 1
            if action == 'MB':
                render = font.render("Movio el espacio hacia abajo", True, [255, 255, 255])
                pos = [100, 50]
                pantalla.blit(render, pos)
            elif action == 'MA':
                render = font.render("Movio el espacio hacia arriba", True, [255, 255, 255])
                pos = [100, 50]
                pantalla.blit(render, pos)
            elif action == 'MD':
                render = font.render("Movio el espacio hacia la derecha", True, [255, 255, 255])
                pos = [100, 50]
                pantalla.blit(render, pos)
            elif action == 'MI':
                render = font.render("Movio el espacio hacia la izquierda", True, [255, 255, 255])
                pos = [100, 50]
                pantalla.blit(render, pos)
            for j in state:
                x = 1
                for k in j:
                    if k == 0:
                        render = font.render(" ", True, [255, 255, 255])
                    else:
                        render = font.render(str(k), True, [255, 255, 255])
                    pos = [x * 20, y * 20]
                    pantalla.blit(render, pos)
                    x += 1
                y += 1
            pygame.display.flip()
            pygame.time.wait(5000)
            pantalla.fill([0, 0, 0])
        interactive = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True