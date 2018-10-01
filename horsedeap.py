from deap import algorithms
from deap import creator
from deap import base
from deap import tools
import random

def generateIndividual():
    individual = list()
    for y in range(0, 8):
        individual.append(list())
        for x in range(0,8):
            if random.randint(0, 10) == 10:
                individual[y].append(1)
            else:
                individual[y].append(0)
    return individual

def createMatrizEval():
    e = list()
    for x in range(0,8):
        e.append(list())
        for y in range(0,8):
            e[x].append(0)
    return e

def evaluateIndividual(individual):
    evalu = createMatrizEval()
    for y in range(0,8):
        for x in range(0,8):
            if individual[y][x] == 1:
                evalu[y][x] = 1
                if (y - 2) >= 0 and (y - 2) < 8 and (x - 1) >= 0 and (x - 1) < 8 and evalu[y - 2][x - 1] == 0:
                    evalu[y - 2][x - 1] = 2
                if (y - 2) >= 0 and (y - 2) < 8 and (x + 1) < 8 and (x - 1) >= 0 and evalu[y - 2][x + 1] == 0:
                    evalu[y - 2][x + 1] = 2
                if (y + 2) < 8 and (y + 2) >= 0 and (x - 1) >= 0 and (x - 1) < 8 and evalu[y + 2][x - 1] == 0:
                    evalu[y + 2][x - 1] = 2
                if (y + 2) < 8 and (y + 2) >= 0 and (x + 1) < 8 and (x - 1) >= 0 and evalu[y + 2][x + 1] == 0:
                    evalu[y + 2][x + 1] = 2
                
                if (y - 1) >= 0 and (y - 1) < 8 and (x - 2) >= 0 and (x - 2) < 8 and evalu[y - 1][x - 2] == 0:
                    evalu[y - 1][x - 2] = 2
                if (y - 1) >= 0 and (y - 1) < 8 and (x + 2) < 8 and (x - 2) >= 0 and evalu[y - 1][x + 2] == 0:
                    evalu[y - 1][x + 2] = 2
                if (y + 1) < 8 and (y + 1) >= 0 and (x - 2) >= 0 and (x - 2) < 8 and evalu[y + 1][x - 2] == 0:
                    evalu[y + 1][x - 2] = 2
                if (y + 1) < 8 and (y + 1) >= 0 and (x + 2) < 8 and (x + 2) >= 0 and evalu[y + 1][x + 2] == 0:
                    evalu[y + 1][x + 2] = 2

    return evalu

d = generateIndividual()
for x in d:
    print(x)

print("Evaluacion: ")
ev = evaluateIndividual(d)
for x in ev:
    print(x)